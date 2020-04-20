import spotipy
import json
import string
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials

#export SPOTIFY_CLIENT_ID='90b9f9fc2ec04d04aae543c938299733'
#export SPOTIFY_CLIENT_SECRET='5b1bcc765ebd4ba2a2bbdb8603705330'


client_credentials_manager = SpotifyClientCredentials('90b9f9fc2ec04d04aae543c938299733',
                                                        '5b1bcc765ebd4ba2a2bbdb8603705330')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_id = 'spotify:user:spotifycharts:playlist:3J43GvmqW6M93WKM1sSjO0'

#most important one
#will be 2d array with song id, name, artist, and lyrics
tracks={}

#array of songs
song_name_array = []

#array of song ids
song_artist_array = []

#array of song lyrics
song_lyrics_array = []

###############################################################3
#gets the song array out of the paylist tracks
temp_song_name_array=[]
offset = 0;
while True:
    response = sp.playlist_tracks(playlist_id,
                                  offset=offset,
                                  fields=('items.track.name,total'))
    
    temp_song_name_array.append(response['items'])
    offset = offset + len(response['items'])

    if len(response['items']) == 0:
        break

temp_song_name_array.pop(1)

#puts it into a manipulative array
temp_song_name_array2=[]
for i in temp_song_name_array:
    for a in range(14): #try to not make this static down the road
        temp_song_name_array2.append(i[a])

#manipulates array and creates a separate list of strictly song names
temp_song_name_array3 = []
for i in temp_song_name_array2:
    temp_song_name_array3.append(i['track']['name'])

for i in temp_song_name_array3:
    song_name_array.append(i) 

del temp_song_name_array, temp_song_name_array2, temp_song_name_array3

###########################################################################
#try to generalize above
#time for artists

temp_song_artist_array=[]
offset = 0;
while True: #got this part from an article
    response = sp.playlist_tracks(playlist_id,
                                  offset=offset,
                                  fields=('items.track.artists,total'))
    
    temp_song_artist_array.append(response['items'])
    offset = offset + len(response['items'])

    if len(response['items']) == 0:
        break

temp_song_artist_array.pop(1)

#puts it into a manipulative array
temp_song_artist_array2=[]
for i in temp_song_artist_array:
    for a in range(14): #try to not make this static down the road
        temp_song_artist_array2.append(i[a])

#manipulates array and creates a separate list of strictly song names
temp_song_artist_array3 = []
for i in temp_song_artist_array2:
    temp_song_artist_array3.append(i['track']['artists'])

temp_song_artist_array4 = []
for i in temp_song_artist_array3:
    temp_song_artist_array4.append(i[0]['name'])

for i in temp_song_artist_array4:
    song_artist_array.append(i)

del temp_song_artist_array, temp_song_artist_array2, temp_song_artist_array3, temp_song_artist_array4

##############################################################
#saving lyrics

import lyricsgenius

genius = lyricsgenius.Genius("DarqZVpt40MVjo3IvGD-njXzLaAptNedLk2SS5QydS9vAcgS8LHHraOZglPEMEm3")

for i in range(14):
    song_lyrics_array.append(genius.search_song(song_name_array[i],song_artist_array[i]).lyrics)

#############################################################
#last steps

a = ""
for i in range(14):
    a = "Song {}".format(i+1)
    tracks[a] = ({
        "Name" : song_name_array[i],
        "Artist" : song_artist_array[i],
        "Lyrics" : song_lyrics_array[i]
    })

outfile =  open('track_lyrics.json', 'w')

json.dump(tracks,outfile,indent=5)

outfile.close()