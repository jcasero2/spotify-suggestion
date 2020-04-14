import numpy as np
import json
class lyr_matrix:
	def __init__(self, pref_json, pool_json):
		pref_dict, pref_num_words = createPref(pref_json)
		self.pref_string = makePrefString(pref_dict, pref_num_words)
		self.pool_string = makePoolString(pool_json, pref_dict, pref_num_words)

def insert(source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]

def removeMarks(word):
	return ''.join(ch for ch in word if ch.isalnum())

# creates the preference matrix 
def createPref(pref_json):
	pref_dict = {}
	num_words = 0
	with open(pref_json, 'r') as json_file:
		playlist_dict = json.load(json_file)
		for song in playlist_dict['songs']:
			for word in song['lyrics'].split():
				#this is hopefully redundant
				if len(word) > 4:
					word = removeMarks(word.lower())
					pref_dict[word] = pref_dict.get(word, 0) + 1 
					num_words += 1
	return pref_dict, num_words

def makePrefString(pref_dict, pref_num_words):
	pref_string = ""
	counter = 0
	for val in pref_dict.values():
		pref_string += str(val/pref_num_words)
		if counter != len(pref_dict) - 1:
			pref_string += ";"
		counter += 1
	return pref_string

def makePoolString(pool_json, pref_dict, pref_num_words):
	pool_string = ""
	for i in range(len(pref_dict) - 1):
		pool_string += ";"
	with open(pool_json, 'r') as json_file:
		playlist_dict = json.load(json_file)
		for song in playlist_dict['songs']:
			song_dict = {x:0 for x in pref_dict.keys()}
			song_num_words = 0
			for word in song['lyrics'].split():
				if len(word) > 4:
					word = removeMarks(word.lower())
					if word in song_dict:
						song_dict[word] += 1
						song_num_words += 1

			beg_index = 0
			counter = 0
			for val in song_dict.values():
				temp_string = " "
				temp_string += str(val/song_num_words)
				if counter != len(song_dict) - 1:
					beg_index = pool_string.find(";", beg_index)
					pool_string = insert(pool_string, temp_string, beg_index)
				else:
					pool_string += temp_string
				beg_index += len(temp_string)
				beg_index += 1
				counter += 1
	return pool_string