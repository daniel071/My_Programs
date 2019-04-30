from phue import Bridge
from myInfo import getHueIP
import random

print("Attempting to connect to hue")
b = Bridge(getHueIP())

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()

print("Connected to hue")

lights_list = b.get_light_objects('list')
light = lights_list

for l in light:
    if l.name == 'Hue color lamp 2':
        print(l.hue)
        print(l.colortemp_k)
        l.transitiontime = 0
        l.saturation = random.randint(0, 254)
        l.brightness = random.randint(0, 254)
        l.hue = random.randint(0, 65535)
