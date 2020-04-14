import numpy as np
class lyr_matrix:
	def __init__(self, pref_txt, pool_txt):
		pref_matrix, pref_num_words = createPref(pref_txt)
		self.pref_string = makePrefString(pref_matrix, pref_num_words)


def removeMarks(word):
	return ''.join(ch for ch in word if ch.isalnum())

# creates the preference matrix 
def createPref(pref_txt):
	pref = {}
	num_words = 0
	with open(pref_txt,'r') as file:
		for line in file:
			for word in line.split():
				word = removeMarks(word.lower())
				pref[word] = pref.get(word, 0) + 1 
				num_words += 1
	return pref, num_words

def makePrefString(pref_matrix, pref_num_words):
	pref_string = ""
	counter = 0
	for val in pref_matrix.values():
		pref_string += str(val/pref_num_words)
		if counter != len(pref_matrix) - 1:
			pref_string += ";"
		counter += 1
	return pref_string