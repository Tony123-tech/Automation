import pygame
import chess
import chess.engine
import os
import sys
import random
import time

pygame.init()

WIDTH, HEIGHT = 700, 800
BOARD_SIZE = 8
SQUARE_SIZE = 78
MARGIN = 18

WHITE_SQ = (240, 217, 181)
BLACK_SQ = (181, 136, 99)
HIGHLIGHT = (255, 255, 0, 100)
MOVE_HIGHLIGHT = (0, 255, 0, 80)
LAST_MOVE = (255, 255, 150, 100)
CHECK_HIGHLIGHT = (255, 0, 0, 150)

MENU_BG = (20, 20, 30)
MENU_TITLE = (220, 200, 80)
MENU_TEXT = (200, 200, 210)
MENU_BUTTON = (50, 50, 70)
MENU_BUTTON_HOVER = (80, 80, 120)
MENU_BUTTON_SELECTED = (60, 80, 100)
MENU_BUTTON_START = (50, 120, 50)
MENU_BUTTON_START_HOVER = (70, 160, 70)

class ChessGame:
    def __init__(self):
        # Self Settings
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess Master")
        self.clock = pygame.time.Clock()
        self.font_small = pygame.font.Font(None, 24)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_large = pygame.font.Font(None, 48)
        self.font_xl = pygame.font.Font(None, 64)
        self.font_clock = pygame.font.Font(None, 52)
        self.board = chess.Board()
        self.selected = None
        self.valid_moves = []
        self.move_history = []
        self.game_over = False
        self.game_result = ""
        self.player_color = chess.WHITE
        self.ai_color = chess.BLACK
        self.ai_thinking = False
        self.ai_depth = 20
        self.time_control = "10"
        self.time_controls = {
            "1": {"name": "Bullet", "minutes": 1},
            "3": {"name": "Blitz", "minutes": 3},
            "10": {"name": "Rapid", "minutes": 10},
            "20": {"name": "Classical", "minutes": 20}
        }
        self.white_time = 10 * 60
        self.black_time = 10 * 60
        self.last_move_time = time.time()
        self.clock_running = False
        self.clock_paused = False
        self.hover_button = None
        self.engine = None
        self.load_engine()
        self.board_image = self.load_board()
        self.pieces = self.load_pieces()
        self.mode = "AI"
        self.menu_active = True
        self.create_menu()
    
    def load_board(self):
        """Load board image"""
        board_paths = [
            "Boards/dark_wood.png",
            "boards/dark_wood.png",
            "dark_wood.png"
        ]

        for path in board_paths:
            if os.path.exists(path):
                try:
                    board_img = pygame.image.load(path).convert()
                    board_img = pygame.transform.scale(board_img, (BOARD_SIZE * SQUARE_SIZE, BOARD_SIZE * SQUARE_SIZE))
                    print(f"Board loaded: {path}")
                    return board_img
                except Exception as e:
                    print(f"Failed to load board: {e}")
        
        print("Board image not found, using colored squares")
        return None
    
    def load_pieces(self):
        pieces = {}
        
        piece_map = {
            'wp': 'P', 'wn': 'N', 'wb': 'B', 'wr': 'R', 'wq': 'Q', 'wk': 'K',
            'bp': 'p', 'bn': 'n', 'bb': 'b', 'br': 'r', 'bq': 'q', 'bk': 'k'
        }
        
        pieces_folder = "Pieces"
        
        if os.path.exists(pieces_folder):
            print("Loading pieces from 'Pieces' folder...")
            for filename in os.listdir(pieces_folder):
                if filename.endswith('.png'):
                    name = filename.replace('.png', '')
                    if name in piece_map:
                        try:
                            path = os.path.join(pieces_folder, filename)
                            img = pygame.image.load(path).convert_alpha()
                            img = pygame.transform.scale(img, (SQUARE_SIZE - 4, SQUARE_SIZE - 4))
                            pieces[piece_map[name]] = img
                            print(f"  Loaded: {filename}")
                        except Exception as e:
                            print(f"  Failed to load {filename}: {e}")
        else:
            print("Pieces folder not found!")
        
        if len(pieces) == 0:
            print("No piece images found, using Unicode symbols")
            pieces = self.create_unicode_pieces()
        
        return pieces
    
    def create_unicode_pieces(self):
        pieces = {}
        symbols = {
            'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
            'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙'
        }
        
        for symbol, char in symbols.items():
            surf = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
            color = (0, 0, 0) if symbol.islower() else (255, 255, 255)
            font = pygame.font.Font(None, SQUARE_SIZE)
            text = font.render(char, True, color)
            text_rect = text.get_rect(center=(SQUARE_SIZE//2, SQUARE_SIZE//2))
            surf.blit(text, text_rect)
            pieces[symbol] = surf
        
        return pieces
    
    def load_engine(self):
        try:
            stockfish_path = "/Users/Waika/Downloads/stockfish/stockfish-macos-m1-apple-silicon"
            
            if os.path.exists(stockfish_path):
                if not os.access(stockfish_path, os.X_OK):
                    os.chmod(stockfish_path, 0o755)
                self.engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
                print("Stockfish loaded")
            else:
                alt_paths = ["/usr/local/bin/stockfish", "/opt/homebrew/bin/stockfish", "stockfish"]
                for path in alt_paths:
                    if os.path.exists(path):
                        self.engine = chess.engine.SimpleEngine.popen_uci(path)
                        print(f"Stockfish loaded: {path}")
                        break
                
                if not self.engine:
                    print("Stockfish not found. AI disabled.")
                    self.mode = "2P"
        except Exception as e:
            print(f"Engine error: {e}")
            self.mode = "2P"
    
    def create_menu(self):
        self.menu_buttons = []
        y_start = 200

        modes = [
            ("Player vs AI", "AI", (WIDTH//2-110, y_start, 220, 45)),
            ("Player vs Player", "2P", (WIDTH//2-110, y_start+55, 220, 45)),
            ("AI vs AI", "AI_AI", (WIDTH//2-110, y_start+110, 220, 45)),
        ]
        for text, mode, rect in modes:
            self.menu_buttons.append({
                "text": text, 
                "rect": pygame.Rect(rect), 
                "mode": mode, 
                "type": "mode"
            })
        
        time_y = y_start + 190
        time_width = 65
        time_height = 40
        total_width = time_width * 4 + 30
        start_x = WIDTH//2 - total_width//2
        
        time_buttons = [
            ("1m", "1", (start_x, time_y, time_width, time_height)),
            ("3m", "3", (start_x + time_width + 10, time_y, time_width, time_height)),
            ("10m", "10", (start_x + (time_width + 10)*2, time_y, time_width, time_height)),
            ("20m", "20", (start_x + (time_width + 10)*3, time_y, time_width, time_height)),
        ]
        for text, time_val, rect in time_buttons:
            self.menu_buttons.append({
                "text": text, 
                "rect": pygame.Rect(rect), 
                "time": time_val, 
                "type": "time"
            })

        start_width = 180
        start_height = 50
        self.menu_buttons.append({
            "text": "START GAME",
            "rect": pygame.Rect(WIDTH//2 - start_width//2, time_y + 65, start_width, start_height),
            "type": "start"
        })
    
    def draw_menu(self):
        self.screen.fill(MENU_BG)

        title = self.font_xl.render("CHESS MASTER", True, MENU_TITLE)
        title_rect = title.get_rect(center=(WIDTH//2, 110))
        
        shadow = self.font_xl.render("CHESS MASTER", True, (40, 30, 10))
        shadow_rect = shadow.get_rect(center=(WIDTH//2 + 3, 113))
        self.screen.blit(shadow, shadow_rect)
        self.screen.blit(title, title_rect)

        king_symbol = self.font_large.render("♔", True, (200, 180, 50))
        king_rect = king_symbol.get_rect(center=(WIDTH//2, 155))
        self.screen.blit(king_symbol, king_rect)

        subtitle = self.font_medium.render("Choose Your Battle", True, MENU_TEXT)
        sub_rect = subtitle.get_rect(center=(WIDTH//2, 190))
        self.screen.blit(subtitle, sub_rect)
        
        mouse_pos = pygame.mouse.get_pos()
        
        for button in self.menu_buttons:
            rect = button["rect"]
            is_hover = rect.collidepoint(mouse_pos)
            
            if button["type"] == "mode":

                is_selected = button["mode"] == self.mode
                if is_selected:
                    color = MENU_BUTTON_SELECTED
                    border_color = (120, 150, 200)
                elif is_hover:
                    color = MENU_BUTTON_HOVER
                    border_color = (100, 100, 150)
                else:
                    color = MENU_BUTTON
                    border_color = (60, 60, 80)
                
                pygame.draw.rect(self.screen, color, rect, 0, 10)
                pygame.draw.rect(self.screen, border_color, rect, 2, 10)
                
                text_color = (255, 255, 255) if is_selected else MENU_TEXT
                text = self.font_medium.render(button["text"], True, text_color)
                text_rect = text.get_rect(center=rect.center)
                self.screen.blit(text, text_rect)
            
            elif button["type"] == "time":

                is_selected = button["time"] == self.time_control
                if is_selected:
                    color = (60, 100, 60)
                    border_color = (100, 180, 100)
                elif is_hover:
                    color = (50, 60, 50)
                    border_color = (80, 100, 80)
                else:
                    color = (35, 40, 45)
                    border_color = (60, 60, 60)
                
                pygame.draw.rect(self.screen, color, rect, 0, 8)
                pygame.draw.rect(self.screen, border_color, rect, 2, 8)
                
                text_color = (200, 255, 200) if is_selected else (180, 180, 180)
                text = self.font_medium.render(button["text"], True, text_color)
                text_rect = text.get_rect(center=rect.center)
                self.screen.blit(text, text_rect)
            
            elif button["type"] == "start":

                if is_hover:
                    color = MENU_BUTTON_START_HOVER
                    border_color = (120, 200, 120)
                    text_color = (255, 255, 255)
                else:
                    color = MENU_BUTTON_START
                    border_color = (80, 160, 80)
                    text_color = (200, 255, 200)
                
                pygame.draw.rect(self.screen, color, rect, 0, 12)
                pygame.draw.rect(self.screen, border_color, rect, 3, 12)
                
                text = self.font_large.render(button["text"], True, text_color)
                text_rect = text.get_rect(center=rect.center)
                self.screen.blit(text, text_rect)

        status_text = "Stockfish Ready" if self.engine else "AI Disabled (2P mode)"
        status_color = (100, 255, 100) if self.engine else (255, 100, 100)
        status = self.font_small.render(status_text, True, status_color)
        status_rect = status.get_rect(center=(WIDTH//2, HEIGHT - 25))
        self.screen.blit(status, status_rect)

        count_text = f"Pieces: {len(self.pieces)}/12"
        count = self.font_small.render(count_text, True, (150, 150, 160))
        count_rect = count.get_rect(center=(WIDTH//2, HEIGHT - 50))
        self.screen.blit(count, count_rect)
        
        pygame.display.flip()
    
    def handle_menu_click(self, pos):
        """Handle menu click"""
        for button in self.menu_buttons:
            if button["rect"].collidepoint(pos):
                if button["type"] == "mode":
                    if button["mode"] != "2P" and not self.engine:
                        self.mode = "2P"
                    else:
                        self.mode = button["mode"]
                elif button["type"] == "time":
                    self.time_control = button["time"]
                elif button["type"] == "start":
                    self.menu_active = False
                    self.reset_game()
                    return True
        return False
    
    def reset_game(self):
        """Reset game"""
        self.board = chess.Board()
        self.selected = None
        self.valid_moves = []
        self.move_history = []
        self.game_over = False
        self.game_result = ""
        self.ai_thinking = False
        
        minutes = int(self.time_control)
        self.white_time = minutes * 60
        self.black_time = minutes * 60
        self.last_move_time = time.time()
        self.clock_running = True
        
        if self.mode == "AI_AI" and self.engine:
            self.ai_thinking = True
    
    def draw_board(self):
        """Draw board"""
        self.screen.fill((50, 50, 50))
        
        if self.board_image:
            border = pygame.Rect(MARGIN-5, MARGIN-5, BOARD_SIZE*SQUARE_SIZE+10, BOARD_SIZE*SQUARE_SIZE+10)
            pygame.draw.rect(self.screen, (100, 70, 40), border, 0)
            self.screen.blit(self.board_image, (MARGIN, MARGIN))
        else:
            border = pygame.Rect(MARGIN-5, MARGIN-5, BOARD_SIZE*SQUARE_SIZE+10, BOARD_SIZE*SQUARE_SIZE+10)
            pygame.draw.rect(self.screen, (100, 70, 40), border, 0)
            for row in range(BOARD_SIZE):
                for col in range(BOARD_SIZE):
                    x = MARGIN + col * SQUARE_SIZE
                    y = MARGIN + row * SQUARE_SIZE
                    color = WHITE_SQ if (row + col) % 2 == 0 else BLACK_SQ
                    pygame.draw.rect(self.screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))
        
        self.draw_highlights()

        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                col = square % 8
                row = 7 - square // 8
                x = MARGIN + col * SQUARE_SIZE + 2
                y = MARGIN + row * SQUARE_SIZE + 2
                symbol = piece.symbol()
                if symbol in self.pieces:
                    self.screen.blit(self.pieces[symbol], (x, y))
        self.draw_coordinates()
        self.draw_clocks()
        self.draw_status()
    
    def draw_highlights(self):
        """Draw highlights"""
        if self.move_history:
            last = self.move_history[-1]
            for sq in [last.from_square, last.to_square]:
                col = sq % 8
                row = 7 - sq // 8
                x = MARGIN + col * SQUARE_SIZE
                y = MARGIN + row * SQUARE_SIZE
                surf = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
                surf.fill(LAST_MOVE)
                self.screen.blit(surf, (x, y))
        
        if self.selected is not None:
            col = self.selected % 8
            row = 7 - self.selected // 8
            x = MARGIN + col * SQUARE_SIZE
            y = MARGIN + row * SQUARE_SIZE
            surf = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
            surf.fill(HIGHLIGHT)
            self.screen.blit(surf, (x, y))
        
        for move in self.valid_moves:
            col = move.to_square % 8
            row = 7 - move.to_square // 8
            x = MARGIN + col * SQUARE_SIZE + SQUARE_SIZE//2
            y = MARGIN + row * SQUARE_SIZE + SQUARE_SIZE//2
            pygame.draw.circle(self.screen, MOVE_HIGHLIGHT[:3], (x, y), 15)
        
        if self.board.is_check():
            king = self.board.king(self.board.turn)
            if king is not None:
                col = king % 8
                row = 7 - king // 8
                x = MARGIN + col * SQUARE_SIZE
                y = MARGIN + row * SQUARE_SIZE
                surf = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
                surf.fill(CHECK_HIGHLIGHT)
                self.screen.blit(surf, (x, y))
    
    def draw_coordinates(self):
        """Draw coordinates"""
        for i in range(8):
            x = MARGIN + i * SQUARE_SIZE + SQUARE_SIZE//2 - 5
            y = MARGIN + BOARD_SIZE * SQUARE_SIZE + 5
            text = self.font_small.render(chr(97 + i), True, (200, 200, 200))
            self.screen.blit(text, (x, y))
            
            x = MARGIN - 25
            y = MARGIN + (7 - i) * SQUARE_SIZE + SQUARE_SIZE//2 - 10
            text = self.font_small.render(str(i + 1), True, (200, 200, 200))
            self.screen.blit(text, (x, y))
    
    def draw_clocks(self):
        """Draw clocks"""
        clock_y = MARGIN + BOARD_SIZE * SQUARE_SIZE + 10

        color = (255, 255, 255) if self.white_time > 60 else (255, 100, 100)
        white_text = self.font_clock.render(self.format_time(self.white_time), True, color)
        self.screen.blit(white_text, (MARGIN + 10, clock_y))
        
        label = self.font_small.render("WHITE", True, (200, 200, 200))
        self.screen.blit(label, (MARGIN + 10, clock_y + 35))
        

        color = (255, 255, 255) if self.black_time > 60 else (255, 100, 100)
        black_text = self.font_clock.render(self.format_time(self.black_time), True, color)
        black_rect = black_text.get_rect(right=WIDTH - MARGIN - 10)
        black_rect.top = clock_y
        self.screen.blit(black_text, black_rect)
        
        label = self.font_small.render("BLACK", True, (200, 200, 200))
        label_rect = label.get_rect(right=WIDTH - MARGIN - 10)
        label_rect.top = clock_y + 35
        self.screen.blit(label, label_rect)

        control = self.time_controls[self.time_control]
        info = self.font_small.render(f"{control['name']} ({control['minutes']}min)", True, (150, 150, 160))
        info_rect = info.get_rect(center=(WIDTH//2, clock_y + 20))
        self.screen.blit(info, info_rect)

        if not self.game_over and self.clock_running:
            turn = "White" if self.board.turn == chess.WHITE else "Black"
            indicator = self.font_small.render(f"> {turn}'s turn", True, (100, 255, 100))
            indicator_rect = indicator.get_rect(center=(WIDTH//2, clock_y + 45))
            self.screen.blit(indicator, indicator_rect)
    
    def draw_status(self):
        """Draw status"""
        clock_y = MARGIN + BOARD_SIZE * SQUARE_SIZE + 60
        
        if self.game_over:
            status = self.game_result
            color = (255, 200, 0)
        elif self.board.is_check():
            turn = "White" if self.board.turn == chess.WHITE else "Black"
            status = f"{turn} in check!"
            color = (255, 100, 100)
        else:
            turn = "White" if self.board.turn == chess.WHITE else "Black"
            status = f"{turn}'s turn"
            color = (200, 200, 200)
        
        text = self.font_medium.render(status, True, color)
        text_rect = text.get_rect(center=(WIDTH//2, clock_y + 15))
        self.screen.blit(text, text_rect)
        
        move_text = self.font_small.render(f"Move: {self.board.fullmove_number}", True, (200, 200, 200))
        self.screen.blit(move_text, (MARGIN + 10, clock_y + 15))
        
        mode_text = self.font_small.render(f"Mode: {self.mode}", True, (200, 200, 200))
        mode_rect = mode_text.get_rect(right=WIDTH - MARGIN - 10, top=clock_y + 15)
        self.screen.blit(mode_text, mode_rect)
        
        if self.ai_thinking:
            thinking = self.font_small.render("AI thinking...", True, (100, 255, 100))
            thinking_rect = thinking.get_rect(center=(WIDTH//2, clock_y - 15))
            self.screen.blit(thinking, thinking_rect)
    
    def format_time(self, seconds):
        """Format time"""
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        return f"{minutes:02d}:{seconds:02d}"
    
    def get_square_from_click(self, pos):
        """Get square from click"""
        x, y = pos
        if x < MARGIN or x > MARGIN + BOARD_SIZE * SQUARE_SIZE:
            return None
        if y < MARGIN or y > MARGIN + BOARD_SIZE * SQUARE_SIZE:
            return None
        
        col = int((x - MARGIN) // SQUARE_SIZE)
        row = 7 - int((y - MARGIN) // SQUARE_SIZE)
        return row * 8 + col
    
    def handle_click(self, pos):
        """Handle click"""
        if self.menu_active:
            return self.handle_menu_click(pos)
        
        if self.game_over or self.ai_thinking:
            return False
        
        square = self.get_square_from_click(pos)
        if square is None:
            self.selected = None
            self.valid_moves = []
            return False
        
        piece = self.board.piece_at(square)
        
        if self.selected is not None:
            for move in self.valid_moves:
                if move.to_square == square:
                    self.make_move(move)
                    self.selected = None
                    self.valid_moves = []
                    return True
            
            if piece and piece.color == self.player_color:
                self.selected = square
                self.valid_moves = self.get_valid_moves(square)
                return True
            else:
                self.selected = None
                self.valid_moves = []
                return False
        else:
            if piece and piece.color == self.player_color:
                self.selected = square
                self.valid_moves = self.get_valid_moves(square)
                return True
        
        return False
    
    def get_valid_moves(self, square):
        """Get valid moves"""
        return [move for move in self.board.legal_moves if move.from_square == square]
    
    def make_move(self, move):
        """Make a move"""
        self.last_move_time = time.time()
        self.board.push(move)
        self.move_history.append(move)
        self.selected = None
        self.valid_moves = []
        
        self.check_game_over()
        
        if not self.game_over and self.board.turn == self.ai_color and self.engine:
            self.ai_thinking = True
    
    def check_game_over(self):
        """Check game over"""
        if self.board.is_checkmate():
            self.game_over = True
            winner = "Black" if self.board.turn == chess.WHITE else "White"
            self.game_result = f"Checkmate! {winner} wins!"
            self.clock_running = False
        elif self.board.is_stalemate():
            self.game_over = True
            self.game_result = "Stalemate! Draw!"
            self.clock_running = False
        elif self.board.is_insufficient_material():
            self.game_over = True
            self.game_result = "Draw - Insufficient material!"
            self.clock_running = False
        elif self.board.is_fivefold_repetition():
            self.game_over = True
            self.game_result = "Draw - Repetition!"
            self.clock_running = False
        elif self.board.is_fifty_moves():
            self.game_over = True
            self.game_result = "Draw - 50 move rule!"
            self.clock_running = False
    
    def get_ai_move(self):
        """Get AI move"""
        if not self.engine:
            moves = list(self.board.legal_moves)
            return random.choice(moves) if moves else None
        
        try:
            remaining = self.white_time if self.board.turn == chess.WHITE else self.black_time
            thinking_time = min(2.0, max(0.5, remaining / 120))
            result = self.engine.play(self.board, chess.engine.Limit(time=thinking_time, depth=self.ai_depth))
            return result.move
        except:
            return None
    
    def ai_turn(self):
        """AI turn"""
        if not self.ai_thinking or self.board.turn != self.ai_color:
            self.ai_thinking = False
            return
        
        move = self.get_ai_move()
        if move:
            self.last_move_time = time.time()
            self.board.push(move)
            self.move_history.append(move)
            self.check_game_over()
            self.ai_thinking = False
            
            if self.mode == "AI_AI" and not self.game_over and self.engine:
                self.ai_thinking = True
        else:
            self.ai_thinking = False
    
    def update_clocks(self):
        """Update clocks"""
        if not self.clock_running or self.clock_paused or self.game_over:
            return
        
        current_time = time.time()
        elapsed = current_time - self.last_move_time
        
        if self.board.turn == chess.WHITE:
            self.white_time -= elapsed
            if self.white_time <= 0:
                self.white_time = 0
                self.game_over = True
                self.game_result = "Black wins on time! (White ran out)"
                self.clock_running = False
        else:
            self.black_time -= elapsed
            if self.black_time <= 0:
                self.black_time = 0
                self.game_over = True
                self.game_result = "White wins on time! (Black ran out)"
                self.clock_running = False
        
        self.last_move_time = current_time
    
    def run(self):
        """Main loop"""
        running = True
        ai_timer = 0
        clock_timer = 0
        
        while running:
            if not self.menu_active:
                clock_timer += 1
                if clock_timer % 5 == 0:
                    self.update_clocks()
                    clock_timer = 0
            
            if self.ai_thinking and not self.game_over and self.engine:
                ai_timer += 1
                if ai_timer % 10 == 0:
                    self.ai_turn()
                    ai_timer = 0
                    self.redraw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.handle_click(event.pos)
                        self.redraw()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_game()
                        self.redraw()
                    if event.key == pygame.K_ESCAPE:
                        self.menu_active = True
                        self.create_menu()
                        self.redraw()
                    if event.key == pygame.K_SPACE and self.game_over:
                        self.reset_game()
                        self.redraw()
            
            self.redraw()
            self.clock.tick(60)
        
        if self.engine:
            self.engine.quit()
        pygame.quit()
        sys.exit()
    
    def redraw(self):
        if self.menu_active:
            self.draw_menu()
        else:
            self.draw_board()
            pygame.display.flip()

def main():
    print("Looking for:")
    print("  - Boards/dark_wood.png")
    print("  - Pieces/*.png")
    print("=" * 50)
    print("Time Controls:")
    print("  Bullet    - 1 minute")
    print("  Blitz     - 3 minutes")
    print("  Rapid     - 10 minutes")
    print("  Classical - 20 minutes")
    print("=" * 50)
    print("Controls:")
    print("  Click to select and move pieces")
    print("  R - Restart game")
    print("  ESC - Back to menu")
    print("  SPACE - Restart (when game over)")
    print("=" * 50)
    
    game = ChessGame()
    game.run()

if __name__ == "__main__":
    main()