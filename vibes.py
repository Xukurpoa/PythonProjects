from phue import Bridge
import sys
import spotipy
import spotipy.util as util
import time
from datetime import datetime
from datetime import timedelta

def bright(loud):
    return 244.94 * (1.0199 ** loud)

b = Bridge('')
b.connect()
hue = 1
b.create_group('room',[1,2,3,4,5])
#b.set_light(2,'on',True)
b.set_group(1,'on',True)

uri='spotify:track:6CDzDgIUqeDY5g8ujExx2f'
token = util.prompt_for_user_token(username='', scope = 'user-modify-playback-state', client_id="", 
        client_secret="", redirect_uri="http://localhost:8080")
if token:
    sp = spotipy.Spotify(auth=token)
    results = uri
    if results != None:
        #analysis = sp.audio_analysis(results["item"]["uri"])
        analysis = sp.audio_analysis(results)
        iterator = iter(analysis['segments'])
        brightness=32
        val = analysis['segments'][0]
        time_taken = 0
        start_time = time.time()
        prev_time = time.time()
        sp.start_playback(uris=[uri])
        while True:
            #print(""+str(val['loudness_start'])+", " +str(val['loudness_max']))
            if len(val) == 0:
                break
            song_time = time.time()- start_time
            print(""+str(time_taken)+", " +str(song_time))
            #print(val['duration'])
            if time_taken <= song_time:
                time_taken += val['duration']
                val = next(iterator,[])
                #brightness= 108.8 + (val['loudness_start'] * 1.363)
                brightness = bright(val['loudness_start'])
            else:
                move = (time.time() - prev_time)
                jawn = 0
                #print(move)
                if move != 0:
                    jawn = bright(val['loudness_max'] - val['loudness_start'])/move
                brightness += jawn
                prev_time = time.time()
            #print(brightness)
            if hue >= 65535:
                hue = 0
            if brightness > 254:
                brightness = 254
            if brightness < 0:
                brightness = 0
            brightness = int(round(brightness))
            #b.set_group(1,'hue',hue)
            #b.set_group(1,'bri',brightness)
            
            #b.set_light(4,'hue',hue,transitiontime=1)
            #b.set_light(2,'hue',hue,transitiontime=1)
            #b.set_light(1,'hue',hue)
            b.set_light(2,'bri',brightness,transitiontime=1)
            b.set_light(4,'bri',brightness,transitiontime=1)
            #b.set_light(1,'bri',brightness)
            #b.set_light(3,'hue',hue)
            #b.set_light(3,'bri',brightness)
            hue += 5000
            time.sleep(0.1)
            #print(time.time()-start_time)
else:
    print("Can't get token for")  