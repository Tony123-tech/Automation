import pygame
import sys
import random
import numpy as np

class Ball(pygame.sprite.Sprite):
    def __init__(self, groups, screen_width, screen_height, player, opponent, score_func, game_instance):
        super().__init__(groups)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.player = player
        self.opponent = opponent
        self.score_func = score_func
        self.game = game_instance

        self.image = pygame.Surface((24, 24), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, (0, 255, 200), (0, 0, 24, 24))
        self.rect = self.image.get_rect(center=(screen_width / 2, screen_height / 2))
        
        self.speed_x = 0
        self.speed_y = 0
        self.base_speed = 8
        self.active = False
        self.trail = []

    def restart(self):
        self.rect.center = (self.screen_width / 2, self.screen_height / 2)
        self.speed_x = self.base_speed * random.choice((1, -1))
        self.speed_y = self.base_speed * random.choice((0.7, -0.7))
        self.active = True
        self.trail = []

    def update(self, *args, **kwargs):
        if not self.active:
            return

        self.trail.append(self.rect.center)
        if len(self.trail) > 10:
            self.trail.pop(0)

        self.rect.x += self.speed_x
        self.collision('horizontal')
        self.rect.y += self.speed_y
        self.collision('vertical')
        self.check_bounds()

    def draw_trail(self, surface):
        if not self.active:
            return
        for i, pos in enumerate(self.trail):
            alpha = int((i / len(self.trail)) * 150)
            radius = int((i / len(self.trail)) * 12)
            if radius < 1: radius = 1
            
            trail_surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            pygame.draw.ellipse(trail_surf, (0, 255, 200, alpha), (0, 0, radius * 2, radius * 2))
            surface.blit(trail_surf, trail_surf.get_rect(center=pos))

    def collision(self, direction):
        if direction == 'horizontal':
            if pygame.sprite.collide_rect(self, self.player) and self.speed_x > 0:
                self.speed_x *= -1.05
                self.rect.right = self.player.rect.left
                self.game.play_beep(440, 0.1)
            
            if pygame.sprite.collide_rect(self, self.opponent) and self.speed_x < 0:
                self.speed_x *= -1.05
                self.rect.left = self.opponent.rect.right
                self.game.play_beep(440, 0.1)

        if direction == 'vertical':
            if self.rect.top <= 0 and self.speed_y < 0:
                self.speed_y *= -1
                self.rect.top = 0
                self.game.play_beep(330, 0.08)
            if self.rect.bottom >= self.screen_height and self.speed_y > 0:
                self.speed_y *= -1
                self.rect.bottom = self.screen_height
                self.game.play_beep(330, 0.08)

    def check_bounds(self):
        if self.rect.right >= self.screen_width:
            self.game.play_beep(150, 0.3)
            self.score_func('opponent')
            self.active = False
        elif self.rect.left <= 0:
            self.game.play_beep(150, 0.3)
            self.score_func('player')
            self.active = False


class Paddle(pygame.sprite.Sprite):
    def __init__(self, groups, x_pos, y_pos, screen_height):
        super().__init__(groups)
        self.screen_height = screen_height
        self.speed = 0
        self.ai_speed = 6
        self.is_ai = True

        self.image = pygame.Surface((12, 120))
        self.image.fill((230, 230, 250))
        self.rect = self.image.get_rect(center=(x_pos, y_pos))

    def update(self, ball=None):
        if self.is_ai and ball:
            if ball.speed_x < 0:
                if self.rect.centery < ball.rect.centery:
                    self.rect.y += self.ai_speed
                elif self.rect.centery > ball.rect.centery:
                    self.rect.y -= self.ai_speed
        else:
            self.rect.y += self.speed

        if self.rect.top <= 0: self.rect.top = 0
        if self.rect.bottom >= self.screen_height: self.rect.bottom = self.screen_height


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2)
        self.clock = pygame.time.Clock()

        self.screen_width = 1000
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Neon Pong Evolution')

        self.font_score = pygame.font.SysFont('Consolas', 64)
        self.font_timer = pygame.font.SysFont('Consolas', 100)
        self.font_msg = pygame.font.SysFont('Consolas', 36)

        self.player_score = 0
        self.opponent_score = 0
        self.max_score = 5
        self.game_over = False
        self.in_menu = True
        self.countdown_time = 0
        self.timer_active = False

        self.all_sprites = pygame.sprite.Group()

        self.opponent = Paddle(self.all_sprites, 20, self.screen_height/2, self.screen_height)
        self.player = Paddle(self.all_sprites, self.screen_width - 20, self.screen_height/2, self.screen_height)
        self.ball = Ball(self.all_sprites, self.screen_width, self.screen_height, self.player, self.opponent, self.update_score, self)

    def play_beep(self, frequency, duration):
        sample_rate = 22050
        n_samples = int(duration * sample_rate)
        t = np.linspace(0, duration, n_samples, endpoint=False)
        wave = np.sin(2 * np.pi * frequency * t) * 16383
        wave = wave.astype(np.int16)
        stereo_wave = np.vstack((wave, wave)).T
        sound = pygame.sndarray.make_sound(stereo_wave)
        sound.play()

    def update_score(self, side):
        if side == 'player':
            self.player_score += 1
        else:
            self.opponent_score += 1
            
        if self.player_score >= self.max_score or self.opponent_score >= self.max_score:
            self.game_over = True
        else:
            self.start_countdown()

    def start_countdown(self):
        self.countdown_time = pygame.time.get_ticks() + 3000
        self.timer_active = True

    def manage_timer(self):
        if not self.timer_active or self.game_over or self.in_menu:
            return
        
        current_time = pygame.time.get_ticks()
        remaining = self.countdown_time - current_time

        if remaining <= 0:
            self.timer_active = False
            self.ball.restart()
        else:
            seconds = str(int(remaining / 1000) + 1)
            text_surf = self.font_timer.render(seconds, True, (255, 100, 100))
            text_rect = text_surf.get_rect(center=(self.screen_width/2, self.screen_height/2 - 50))
            self.screen.blit(text_surf, text_rect)

    def draw_menu(self):
        title_surf = self.font_timer.render("NEON PONG", True, (0, 255, 200))
        title_rect = title_surf.get_rect(center=(self.screen_width/2, self.screen_height/2 - 100))
        
        mode1_surf = self.font_msg.render("Press 1 for 1-Player Mode (vs AI)", True, (230, 230, 250))
        mode1_rect = mode1_surf.get_rect(center=(self.screen_width/2, self.screen_height/2 + 20))
        
        mode2_surf = self.font_msg.render("Press 2 for 2-Player Mode (Local)", True, (230, 230, 250))
        mode2_rect = mode2_surf.get_rect(center=(self.screen_width/2, self.screen_height/2 + 80))
        
        self.screen.blit(title_surf, title_rect)
        self.screen.blit(mode1_surf, mode1_rect)
        self.screen.blit(mode2_surf, mode2_rect)

    def draw_ui(self):
        if self.in_menu:
            return
            
        pygame.draw.aaline(self.screen, (60, 60, 80), (self.screen_width/2, 0), (self.screen_width/2, self.screen_height))
        
        p_surf = self.font_score.render(str(self.player_score), True, (200, 200, 220))
        o_surf = self.font_score.render(str(self.opponent_score), True, (200, 200, 220))
        self.screen.blit(o_surf, (self.screen_width/4, 30))
        self.screen.blit(p_surf, (self.screen_width * 3/4 - p_surf.get_width(), 30))

        if self.game_over:
            if self.player_score >= self.max_score:
                msg = "PLAYER 2 WINS!" if self.opponent.is_ai == False else "PLAYER WINS!"
                color = (0, 255, 200)
            else:
                msg = "PLAYER 1 WINS!" if self.opponent.is_ai == False else "AI WINS!"
                color = (255, 100, 100)
                
            msg_surf = self.font_timer.render(msg, True, color)
            msg_rect = msg_surf.get_rect(center=(self.screen_width/2, self.screen_height/2 - 50))
            
            sub_surf = self.font_msg.render("Press SPACEBAR to Main Menu", True, (150, 150, 170))
            sub_rect = sub_surf.get_rect(center=(self.screen_width/2, self.screen_height/2 + 50))
            
            self.screen.blit(msg_surf, msg_rect)
            self.screen.blit(sub_surf, sub_rect)

    def reset_game(self):
        self.player_score = 0
        self.opponent_score = 0
        self.game_over = False
        self.in_menu = True
        self.player.speed = 0
        self.opponent.speed = 0

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if self.game_over:
                        if event.key == pygame.K_SPACE:
                            self.reset_game()
                    elif self.in_menu:
                        if event.key == pygame.K_1:
                            self.opponent.is_ai = True
                            self.in_menu = False
                            self.start_countdown()
                        elif event.key == pygame.K_2:
                            self.opponent.is_ai = False
                            self.in_menu = False
                            self.start_countdown()
                    else:
                        if event.key == pygame.K_UP:
                            self.player.speed -= 8
                        if event.key == pygame.K_DOWN:
                            self.player.speed += 8
                        if not self.opponent.is_ai:
                            if event.key == pygame.K_w:
                                self.opponent.speed -= 8
                            if event.key == pygame.K_s:
                                self.opponent.speed += 8

                if event.type == pygame.KEYUP and not self.in_menu and not self.game_over:
                    if event.key == pygame.K_UP:
                        self.player.speed += 8
                    if event.key == pygame.K_DOWN:
                        self.player.speed -= 8
                    if not self.opponent.is_ai:
                        if event.key == pygame.K_w:
                            self.opponent.speed += 8
                        if event.key == pygame.K_s:
                            self.opponent.speed -= 8

            if not self.game_over and not self.in_menu:
                self.all_sprites.update(ball=self.ball)
                self.screen.fill((15, 15, 26))
                if self.in_menu:
                    self.draw_menu()
                else:
                    self.draw_ui()
                self.ball.draw_trail(self.screen)
                self.all_sprites.draw(self.screen)
                self.manage_timer()
            pygame.display.flip()
            self.clock.tick(60)

        if __name__ == '__main__':
            game = Game()
            game.run()
