import customtkinter as ctk
import pyautogui as pg
import time
import threading
import keyboard

pg.FAILSAFE = True
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("99 Nights Of The Forest Script")
root.wm_attributes("-topmost", 1)

font = ctk.CTkFont(family="Helvetica", size=24, weight="bold")
root.geometry("600x400")

def hex_to_rgb(hex_str):
	hex_str = hex_str.lstrip('#')
	return [int(hex_str[i:i+2], 16) for i in (0, 2, 4)]

def rgb_to_hex(rgb):
	return f"#{int(rgb[0]):02x}{int(rgb[1]):02x}{int(rgb[2]):02x}"

class HoverAnimation:
	def __init__(self, widget, start_hex, end_hex, steps=10, delay=15):
		self.widget = widget
		self.start_rgb = hex_to_rgb(start_hex)
		self.end_rgb = hex_to_rgb(end_hex)
		self.steps = steps
		self.delay = delay
		self.current_step = 0
		self.direction = 0
		self.after_id = None
	
	def animate(self):
		if self.direction == 0:
			return

		self.current_step += self.direction

		if self.current_step >= self.steps:
			self.current_step = self.steps
			self.direction = 0
		elif self.current_step <= 0:
			self.current_step = 0
			self.direction = 0

		t = self.current_step / self.steps
		curr_rgb = [
			self.start_rgb[i] + t * (self.end_rgb[i] - self.start_rgb[i])
			for i in range(3)
		]

		curr_hex = rgb_to_hex(curr_rgb)

		self.widget.configure(fg_color=curr_hex, hover_color=curr_hex)

		if self.direction != 0:
			self.after_id = root.after(self.delay, self.animate)

	def fade_in(self, event=None):
		if self.after_id:
			root.after_cancel(self.after_id)
		self.direction = 1
		self.animate()

frame = ctk.CTkFrame(
	master=root,
	fg_color="#0B0C10",
	corner_radius=0
)

frame.pack(fill="both", expand=True)

title_label = ctk.CTkLabel(
	master=frame,
	text="99 Nights Of The Forest Script",
	font=("Segoe UI", 22, "bold"),
	text_color="#45A29E"
)
title_label.pack(pady=(25, 2))

subtitle_label = ctk.CTkLabel(
	master=frame,
	text="99 NIGHTS OF THE FOREST AUTOMATION",
	font=("Segoe UI", 14, "bold"),
	text_color="#C5C6C7"
)
subtitle_label.pack(pady=(0, 20))

status_card = ctk.CTkFrame(
	master=frame,
	fg_color="#1F2833",
	corner_radius=14,
)
status_card.pack(pady=20, padx=20, fill="x")

status_label = ctk.CTkLabel(
	master=status_card,
	text="SYSTEM STATUS: IDLE",
	font=("Segoe UI", 16, "bold"),
	text_color="#e74c3c"
)
status_label.pack(pady=25)

launch_button = ctk.CTkButton(
	master=frame,
	text="LAUNCH AUTOMATION",
	fg_color="#45A29E",
	hover_color="#1F6865",
	text_color="#FFFFFF",
	font=("Segoe UI", 14, "bold"),
	corner_radius=10,
	height=48
)
launch_button.pack(pady=20)

animator = HoverAnimation(launch_button, start_hex="#45A29E", end_hex="#1F6865", steps=12, delay=12)
launch_button.bind("<Enter>", animator.fade_in)
launch_button.bind("<Leave>", animator.fade_in())
root.mainloop()
