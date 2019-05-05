from phue import Bridge
from myInfo import getHueIP
from threading import Thread


print("Attempting to connect to hue")
b = Bridge(getHueIP())

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()

print("Connected to hue")

lights_list = b.get_light_objects('list')
light = lights_list


def huethread():
    global light

    while True:
        for l in light:
            if l.name == 'Hue color lamp 2':
                if l.on is False or l.brightness != 254:
                    l.transitiontime = 0
                    l.on = True
                    # l.colortemp_k = 2700
                    # l.saturation = 143
                    l.brightness = 254
                    # l.hue = 8382
                    print("Color changed")
                else:
                    print("Color skipped")


t1 = Thread(target=huethread)
t2 = Thread(target=huethread)
t3 = Thread(target=huethread)
t4 = Thread(target=huethread)
t5 = Thread(target=huethread)
t6 = Thread(target=huethread)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
