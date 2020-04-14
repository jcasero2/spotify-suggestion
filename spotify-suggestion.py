import numpy as np
import scipy.sparse.linalg as sp
from lyr_matrix import lyr_matrix as lm

# Let q be our query vector
pref = np.mat('0; 0; 1')
songs = np.mat('1 0 0 .2 .65 .50 .9;0 1 0.7 0.4 .35 .5 .1;0 0 0.3 0.4 0 0 0')
songs_rows, songs_cols = songs.shape

mSystem = lm('pref.json', 'pref.json')
#print(mSystem.pref_string)
pref2 = np.mat(mSystem.pref_string)
print(mSystem.pref_dict)
print(pref2)

print ("q:")
print(pref)
print("")
print("d:")
print(songs)
print("")

# song = column vector i in matrix songs
# pref_T = transpose of pref
# num = dot product of pref_T and song
# pref_norm = length of q
# song_norm = length of song
results_str = ""
pref_T = pref.T
pref_norm = np.linalg.norm(pref)
i = 0
for i in range(0, songs_cols):
	song = songs[:,i]
	num = (np.dot(pref_T, song)).item(0)
	song_norm = np.linalg.norm(song)
	denom = pref_norm * song_norm
	result = 0
	if denom != 0:
		result = num/denom
	results_str += str(result)
	if i < songs_cols - 1:
		results_str += ";"

results = np.mat(results_str)
print("results:")
print(results)
