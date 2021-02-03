import sys
import spotipy
import spotipy.util as util
import os
from datetime import datetime
import time
 
curSong = ""
for x in range(10):
    #token = util.prompt_for_user_token(username='', scope = 'user-read-playback-state', client_id=os.environ['SPOTIPY_CLIENT_ID'], 
       # client_secret=os.environ['SPOTIPY_CLIENT_SECRET'], redirect_uri=os.environ['SPOTIPY_REDIRECT_URI'])
    if token:
        
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_playing_track()
        #print(results['is_playing'])
        now = datetime.now()
        file = open("song_list.txt","a+")
        if results['is_playing'] == True and curSong != results["item"]["uri"]:
            #print(file.read())
            file.write(""+results["item"]["uri"]+","+now.strftime("%m/%d/%Y,%H:%M:%S")+"\n")
            curSong = results["item"]["uri"]
            file.close
            time.sleep(1)
    else:
        print("Can't get token for", username)
    
    