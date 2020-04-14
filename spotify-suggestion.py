import numpy as np
import scipy.sparse.linalg as sp
import json
from heapq import heappush, nlargest
from lyr_matrix import lyr_matrix as lm

mSystem = lm('pref.json', 'pool.json')
pref = np.mat(mSystem.pref_string)
# print(mSystem.pool_string)
pool = np.mat(mSystem.pool_string)
pool_rows, pool_cols = pool.shape

print ("pref:")
print(pref)
print("")
print("pool:")
print(pool)
print("")

# song = column vector i in matrix songs
# pref_T = transpose of pref
# num = dot product of pref_T and song
# pref_norm = length of q
# song_norm = length of song
results_str = ""
pref_T = pref.T
pref_norm = np.linalg.norm(pref)
for i in range(0, pool_cols):
	song = pool[:,i]
	num = (np.dot(pref_T, song)).item(0)
	song_norm = np.linalg.norm(song)
	denom = pref_norm * song_norm
	result = 0
	if denom != 0:
		result = num/denom
	results_str += str(result)
	if i < pool_cols - 1:
		results_str += ";"

results = np.mat(results_str)
print("results:")
print(results)
print("")

results_list = []
for i in range(0, pool_cols):
	heappush(results_list, (results[i,0], i))
index_recom = nlargest(5, results_list)

with open('pref.json', 'r') as json_file:
	pref_json = json.load(json_file)
	tempStr = pref_json['playlistName']
	print("According to playlist:", tempStr)

with open('pool.json', 'r') as json_file:
	pool_json = json.load(json_file)
	print("Top", len(index_recom), "recommendations:")
	for i in range(0, len(index_recom)):
		temp_index = index_recom[i][1]
		tempStr = str(i + 1)
		tempStr += ". "
		tempStr += pool_json['songs'][temp_index]['title']
		tempStr += " – "
		tempStr += pool_json['songs'][temp_index]['artist']
		print(tempStr)

