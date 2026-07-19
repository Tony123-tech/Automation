import pyautogui
import time

print("=" * 50)
print("🖱️  Mouse Position Tracker")
print("=" * 50)
print("Move your mouse around.")
print("Position will update every 0.5 seconds.")
print("Press Ctrl+C to stop.")
print("=" * 50)
print()

try:
    while True:
        # Get current mouse position
        x, y = pyautogui.position()
        
        # Clear previous line and print new position
        print(f"\r📍 Position: ({x:>4}, {y:>4})", end="", flush=True)
        
        time.sleep(0.5)
        
except KeyboardInterrupt:
    print("\n\n✅ Stopped! Last position saved.")
    print(f"📌 Final position: ({x}, {y})")
    print("\n💡 Use these coordinates in neal.py")
