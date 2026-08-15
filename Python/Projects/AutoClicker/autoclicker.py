import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

d = 0.001
btn = Button.left

start_key = KeyCode(char="s")
exit_key = KeyCode(char="e")

class AutoClicker(threading.Thread):
    def __init__(self, d, btn):
        super().__init__()
        self.d = d
        self.btn = btn
        self.clicking = False
        self.active = True

    def start_click(self):
        self.clicking = True
    def stop_click(self):
        self.clicking = False
    def exit(self):
        self.stop_click()
        self.active = False
    def run(self):
        while self.active:
            while self.clicking:
                mouse.click(self.btn)
                time.sleep(self.d)

mouse = Controller()

clicker = AutoClicker(d, btn)
clicker.start()

def on_press(k):
    if k == start_key:
        if clicker.clicking:
            clicker.stop_click()
        else:
            clicker.start_click()
    elif k == exit_key:
        clicker.exit()
        return False

with Listener(on_press=on_press) as listener:
    listener.join()