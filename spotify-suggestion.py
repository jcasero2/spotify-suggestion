import numpy as np
import scipy.sparse.linalg as sp
from lyr_matrix import lyr_matrix as lm

mSystem = lm('pref.json', 'pool.json')
pref = np.mat(mSystem.pref_string)
print(mSystem.pool_string)
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
i = 0
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
