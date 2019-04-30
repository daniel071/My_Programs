from phue import Bridge
from myInfo import getHueIP
import time

print("Attempting to connect to hue")
b = Bridge(getHueIP())

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()

print("Connected to hue")

# oldHue = b.get_light(2, 'hue')
# loop = 0
# while loop <= 1:
#     print(loop)
#     b.set_light(2, "hue", 30202, transitiontime=2)
#     time.sleep(0.5)
#     b.set_light(2, "hue", oldHue, transitiontime=2)
#     time.sleep(0.5)
#     loop = loop + 1
#
# b.set_light(2, "hue", oldHue, transitiontime=2)
# time.sleep(2)


# while True:
    # print(b.get_light(2, 'hue'))
    # time.sleep(1)