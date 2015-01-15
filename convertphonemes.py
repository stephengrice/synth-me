import phonemes

def words_to_phonemes(words):
	# Takes list of words
	result = []

	for word in words:
		result.append(word_to_phoneme(word))
	return result

def word_to_phoneme(word):
	# 1. Check if the word has been learned

	# 2. If not, take an educated guess

	pass