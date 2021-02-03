from phue import Bridge

import time
#spotify:track:6CDzDgIUqeDY5g8ujExx2f
#b = Bridge()
b.connect()
hue = 1
b.create_group('down',[2,4])
#b.set_light(,'off',True)
#b.set_group(1,'on',True)
#top light is 4
while True:
    if hue >= 65535:
        hue = 0
    #b.set_light(2,'hue',hue,transitiontime=1)
    #b.set_light(5,'hue',hue,transitiontime=1)
    b.set_group(1,'hue',hue,transitiontime=1)
    #b.set_light(4,'hue',4000)
    #b.set_light(1,'hue',45000)
    time.sleep(0.1)
    hue+=2500
    #print(hue) 
