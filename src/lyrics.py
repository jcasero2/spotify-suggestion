import spotipy
import json
import sys
import string
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials

if len(sys.argv) > 3:
    client_credentials_manager = SpotifyClientCredentials(sys.argv[1],sys.argv[2])
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    if len(sys.argv) == 5:
        temp = sys.argv[4]
        if temp.find('https://open.spotify.com/playlist/') != -1:
            temp = temp.replace("https://open.spotify.com/playlist/","")
            playlist_id = 'spotify:user:spotifycharts:playlist:{}'.format(temp)
        else:
            playlist_id = 'spotify:user:spotifycharts:playlist:{}'.format(temp)
    else:
        playlist_id = 'spotify:user:spotifycharts:playlist:3J43GvmqW6M93WKM1sSjO0'

    #most important one
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
    
    #puts it into a manipulative array and gets playlist size
    temp_song_name_array2=[]
    count = 0

    for i in temp_song_name_array:
        for a in i: #try to not make this static down the road
            temp_song_name_array2.append(a)
            count = count + 1
    
    playlist_size = count

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
        for a in i: #try to not make this static down the road
            temp_song_artist_array2.append(a)

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

    genius = lyricsgenius.Genius(sys.argv[3])

    for i in range(playlist_size):
        song_lyrics_array.append(genius.search_song(song_name_array[i],song_artist_array[i]).lyrics)

    #############################################################
    #last steps

    a = ""
    for i in range(playlist_size):
        a = "Song {}".format(i+1)
        tracks[a] = ({
            "Name" : song_name_array[i],
            "Artist" : song_artist_array[i],
            "Lyrics" : song_lyrics_array[i]
        })

    outfile =  open('track_lyrics.json', 'w')

    json.dump(tracks,outfile,indent=5)

    outfile.close()

else:
    print("missing essential args")