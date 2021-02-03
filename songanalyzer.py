import sqlite3
from sqlite3 import Error
import spotipy
import spotipy.util as util
import sys
import lyricsgenius
import os
from collections import Counter
import time
def remove_redudant(string):
    string = string.replace('!',' ')
    
    string = string.replace('.',' ')
    string = string.replace('?',' ')
    string = string.replace('-',' ')
    string = string.replace(':',' ')
    string = string.replace(';',' ')
    string = string.replace(',',' ')
    string = string.replace('"',' ')
    string = string.replace('\n',' ')
    string = string.replace('(',' ')
    string = string.replace(')',' ')
    return string

try:
    token = util.prompt_for_user_token(username='', scope = 'user-read-playback-state', client_id=os.environ['SPOTIPY_CLIENT_ID'], 
            client_secret=os.environ['SPOTIPY_CLIENT_SECRET'], redirect_uri=os.environ['SPOTIPY_REDIRECT_URI'])
    if token:
        sp = spotipy.Spotify(auth=token)
        genius = lyricsgenius.Genius("WTNsrPdygCItBIYfSRtiMX6kNxttt-SFQge38sDZcpvmoc4X99s9VjE65XeG-SGM")
        genius.verbose = False # Turn off status messages
        genius.remove_section_headers = True # Remove section headers (e.g. [Chorus]) from lyrics when searching
        counted=Counter('a')
        counted.update('a')
        
        #print(counted.most_common())
        with open("song_list.txt",'r') as songs:
            for line in songs:
                uri = line.split(',')[0]
                song=sp.track(uri)
                song = genius.search_song(str(song['name']), song["artists"][0]["name"])
                if song != None:
                    lyrics = song.lyrics.lower()
                    #print(song.lyrics)
                    lyrics = remove_redudant(lyrics)
                    listLyrics = lyrics.split()
                    counted.update(listLyrics)
                    print(lyrics)
                else:
                    print(uri)
                time.sleep(2)
            print(counted)
            
except NameError as err:
    print("Name error: {0}".format(err))
