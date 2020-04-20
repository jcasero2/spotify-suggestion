import spotipy
import json
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials

#export SPOTIFY_CLIENT_ID='90b9f9fc2ec04d04aae543c938299733'
#export SPOTIFY_CLIENT_SECRET='5b1bcc765ebd4ba2a2bbdb8603705330'


client_credentials_manager = SpotifyClientCredentials('90b9f9fc2ec04d04aae543c938299733',
                                                        '5b1bcc765ebd4ba2a2bbdb8603705330')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_id = 'spotify:user:spotifycharts:playlist:3J43GvmqW6M93WKM1sSjO0'

#most important one
track_array=[]

#array of songs
song_name_array = []

#array of artist ids
song_id_array = []

#array of song ids
song_artist_array = []

###############################################################3
#gets the song array out of the paylist tracks
temp_song_name_array=[]
offset = 0;
while True:
    response = sp.playlist_tracks(playlist_id,
                                  offset=offset,
                                  fields=('items.track.name,total'))
    #pprint(response['items'])
    temp_song_name_array.append(response['items'])
    offset = offset + len(response['items'])

    if len(response['items']) == 0:
        break

temp_song_name_array.pop(1)
#pprint(temp_song_name_array)

#puts it into a manipulative array
temp_song_name_array2=[]
for i in temp_song_name_array:
    for a in range(1,14): #try to not make this static down the road
        temp_song_name_array2.append(i[a])

#manipulates array and creates a separate list of strictly song names
temp_song_name_array3 = []
for i in temp_song_name_array2:
    temp_song_name_array3.append(i['track']['name'])

for i in temp_song_name_array3:
    song_name_array.append(i.encode('ascii', 'ignore')) 

pprint(song_name_array)
del temp_song_name_array, temp_song_name_array2, temp_song_name_array3

###########################################################################
#try to generalize above
#fuck no we can't, maybe put into function

temp_song_id_array=[]
offset = 0;
while True: #got this part from an article
    response = sp.playlist_tracks(playlist_id,
                                  offset=offset,
                                  fields=('items.track.id,total'))
    #pprint(response['items'])
    temp_song_id_array.append(response['items'])
    offset = offset + len(response['items'])

    if len(response['items']) == 0:
        break

temp_song_id_array.pop(1)
#pprint(temp_song_name_array)

#puts it into a manipulative array
temp_song_id_array2=[]
for i in temp_song_id_array:
    for a in range(1,14): #try to not make this static down the road
        temp_song_id_array2.append(i[a])

#manipulates array and creates a separate list of strictly song names
temp_song_id_array3 = []
for i in temp_song_id_array2:
    temp_song_id_array3.append(i['track']['id'])

for i in temp_song_id_array3:
    song_id_array.append(i.encode('ascii', 'ignore')) 

pprint(song_id_array)
del temp_song_id_array, temp_song_id_array2, temp_song_id_array3

#######################################################################
#time for artists

temp_song_artist_array=[]
offset = 0;
while True: #got this part from an article
    response = sp.playlist_tracks(playlist_id,
                                  offset=offset,
                                  fields=('items.track.artists,total'))
    #pprint(response['items'])
    temp_song_artist_array.append(response['items'])
    offset = offset + len(response['items'])

    if len(response['items']) == 0:
        break

temp_song_artist_array.pop(1)
#pprint(temp_song_name_array)

#puts it into a manipulative array
temp_song_artist_array2=[]
for i in temp_song_artist_array:
    for a in range(1,14): #try to not make this static down the road
        temp_song_artist_array2.append(i[a])

#manipulates array and creates a separate list of strictly song names
temp_song_artist_array3 = []
for i in temp_song_artist_array2:
    temp_song_artist_array3.append(i['track']['artists'])

temp_song_artist_array4 = []
for i in temp_song_artist_array3:
    temp_song_artist_array4.append(i[0]['name'])

for i in temp_song_artist_array4:
    song_artist_array.append(i.encode('ascii', 'ignore'))

pprint(song_artist_array)
del temp_song_artist_array, temp_song_artist_array2, temp_song_artist_array3, temp_song_artist_array4
