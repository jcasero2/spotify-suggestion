import json
import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

#export SPOTIFY_CLIENT_ID='90b9f9fc2ec04d04aae543c938299733'
#export SPOTIFY_CLIENT_SECRET='5b1bcc765ebd4ba2a2bbdb8603705330'

#spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name']))

##############################

if __name__ == '__main__':
    if len(sys.argv) > 0:
        username = sys.argv[1]
        user_id = sys.argv[2]
        user_secret = sys.argv[3]
        user_redirect = sys.argv[4]
    else:
        print("Whoops, need your playlist!")
        print("usage: python user_playlists.py [username]")
        sys.exit()

    token = util.prompt_for_user_token(username, 'user-library-read', user_id, user_secret, user_redirect)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
    else:
        print("Can't get token for", username)
    #need to first get playlist

    #need to then get the playlist song title, artist and users

    #add them to a 2D array or vector or list or whatnot

    #for each song, output each of the lyrics to a csv file

    #return the song, artist and lyrics in json format