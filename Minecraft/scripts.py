import customtkinter as ctk
import threading


# Configure customtkinter appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Minecraft Scripts")
root.geometry("400x300")
root.resizable(False, False)

def start_auto_farm():
    thread = threading.Thread(target=auto_farm, daemon=True)
    thread.start()

def auto_farm():
    pass
    



auto_farm_button = ctk.CTkButton(root, text="Auto Farm", command=auto_farm, font=("Arial", 14, "bold"))
auto_farm_button.pack(pady=20)

root.mainloop()