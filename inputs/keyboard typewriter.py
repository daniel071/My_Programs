from pynput.keyboard import Key, Controller
import time
print("Input words:")
words = input()

time.sleep(3)

keyboard = Controller()
for char in words:
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.012)
