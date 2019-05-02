from pynput.keyboard import Key, Controller
from myInfo import getSQLPass
import time


time.sleep(2)

keyboard = Controller()
for char in getSQLPass():
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.05)
