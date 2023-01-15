# The following programs must be installed:
# pip install pyautogui
# pip install pynput

import pyautogui
from pynput.keyboard import Listener

def on_press(key):
    try:
        if key.char == 'p': # You can change the key that is being listened for in the code to any key that you want.
            x, y = pyautogui.position()
            print(f"Mouse is at x: {x} y: {y}") # f is formatted string literals
            # You can also use print("Mouse is at x: {} y: {}".format(x,y)) but that is using str.format instead (same output though)
    except AttributeError:
        pass

with Listener(on_press=on_press) as listener:
    listener.join()

# This program uses the pyautogui.position() function to get the current x,y coordinates of the mouse cursor, and prints them to the console. 
# The program also uses the pynput library to listen for key presses. 
# When the 'p' key is pressed, the current mouse position is logged to the console.