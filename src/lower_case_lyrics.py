with open("bb.txt", 'r') as file:
	temp = ""
	for line in file:
		for word in line.split():
			#this is hopefully redundant
			word = ''.join(ch for ch in word if ch.isalnum())
			word = word.lower()
			temp += word
			temp += " "
	print(temp)