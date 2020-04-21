# spotify-suggestion
Jorge Casero <jcasero@umich.edu><br />
Sid Murthy <smurthy@umich.edu>

## Description
Program that takes a Spotify playlist and recommends a song to add from another playlist based on the similarities between the lyrics from all the songs in the playlist and each song that can be potentially recommended.

## Linear Algebra
Following the Vector Space Model, this program calculates the angle that is formed between the column vector formed by the frequency of the words on the current playlist and the frequency of those same words on the possible suggested songs.

## Requirements
pip3 install PyLyrics<br />
pip3 install numpy

## Spotify/Genius API Client requirements
You need:
Spotify API Client ID
Spotify API Client Secret
Genius API Client Access Token

- When running program, format is python3 lyrics.py --Spotify client ID-- --Spotify client secret-- --Genius client access token--

## Languages
Python (Python 3 needed)
