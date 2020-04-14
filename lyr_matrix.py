import numpy as np
import json
class lyr_matrix:
	def __init__(self, pref_json, pool_json):
		self.pref_dict, pref_num_words = createPref(pref_json)
		self.pref_string = makePrefString(self.pref_dict, pref_num_words)


def removeMarks(word):
	return ''.join(ch for ch in word if ch.isalnum())

# creates the preference matrix 
def createPref(pref_json):
	pref = {}
	num_words = 0
	with open(pref_json, 'r') as json_file:
		playlist_dict = json.load(json_file)
		for song in playlist_dict['songs']:
			for word in song['lyrics'].split():
				#this is hopefully redundant
				if len(word) > 4:
					word = removeMarks(word.lower())
					pref[word] = pref.get(word, 0) + 1 
					num_words += 1
	return pref, num_words

def makePrefString(pref_dict, pref_num_words):
	pref_string = ""
	counter = 0
	for val in pref_dict.values():
		pref_string += str(val/pref_num_words)
		if counter != len(pref_dict) - 1:
			pref_string += ";"
		counter += 1
	return pref_string