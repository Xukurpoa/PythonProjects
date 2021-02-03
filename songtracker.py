import sys
import spotipy
import spotipy.util as util
import os
from datetime import datetime
import time
 
curSong = ""
#C:/python/spotify-analyzer/songtracker.py
while True:
    try:
        token = util.prompt_for_user_token(username='', scope = 'user-read-playback-state', client_id=os.environ['SPOTIPY_CLIENT_ID'], 
            client_secret=os.environ['SPOTIPY_CLIENT_SECRET'], redirect_uri=os.environ['SPOTIPY_REDIRECT_URI'])
        if token:
            sp = spotipy.Spotify(auth=token)
            results = sp.current_user_playing_track()
            if results != None:
                now = datetime.now()
                #print(results["item"]["uri"]+" "+curSong+" "+str(results['is_playing']))
                if results['is_playing'] == True and curSong != results["item"]["uri"]:
                    print(""+results["item"]["uri"]+","+now.strftime("%m/%d/%Y,%H:%M:%S")+","+str(results["item"]["popularity"])+"\n")
                    file = open("song.txt","a+")
                    file.write(""+results["item"]["uri"]+","+now.strftime("%m/%d/%Y,%H:%M:%S")+","+str(results["item"]["popularity"])+"\n")
                    curSong = results["item"]["uri"]
                    file.close()
        else:
            print("Can't get token for")
    except:
        print("timeout occured")
    time.sleep(30)  