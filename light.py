import phue
from phue import Bridge

import time
#spotify:track:6CDzDgIUqeDY5g8ujExx2f
#b = Bridge()
b.connect()
hue = 1
b.create_group('room',[1,2,3,4,5])
#b.set_light(2,'on',True)
b.set_group(1,'on',True)
#top light is 4
delta = 250
while True:
    if hue >= 65535:
        hue = 0
    b.set_group(1,'hue',hue,transitiontime=1)
    hue+=delta
    time.sleep(0.3)
    
