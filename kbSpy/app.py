from pynput.keyboard import Key, Listener
global listener_
import sys
def on_press(key):
    pass
def on_release(key):
    char = str(key).replace("'", "")
    if "Key" in char:
        if "Key.space" in char:
            sys.stdout.write(" ")
        elif "enter" in char:
            sys.stdout.write("\n")
        else:
            print()
            sys.stdout.write("> "+char)
            print()
    else:
        sys.stdout.write(char)
    sys.stdout.flush()
    if key == Key.esc:
        # Stop listener
        return False

print("<Listening> ON\n")
# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
