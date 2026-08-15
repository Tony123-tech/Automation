import customtkinter as ctk

# Configure customtkinter appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("+1 Speed Keyboard Escape")
root.geometry("400x300")
root.resizable(False, False)

def auto_farm():
    pass

auto_farm_button = ctk.CTkButton(root, text="Auto Farm", command=auto_farm, font=("Arial", 14, "bold"))
auto_farm_button.pack(pady=20)

root.mainloop()