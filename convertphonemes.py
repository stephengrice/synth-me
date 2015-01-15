import phonemes

def words_to_phonemes(words):
	# Takes list of words
	result = []

	for word in words:
		result.append(word_to_phoneme(word))
	return result

def word_to_phoneme(word):
	# 1. Check if the word has been learned
		# Connect to DB
		# Select all where word
		# Convert phoneme list to python list; return

	# 2. If not, take an (un)educated guess
	result = guess_letters(word)

	return result

def guess_letters(word):
	word = word.lower()
	result = []
	for l in word:
		if l == 'a':
			result.append(phonemes.VOWEL_A)
		elif l == 'b':
			result.append(phonemes.CONS_B)
		elif l == 'c':
			result.append(phonemes.CONS_K)
		elif l == 'd':
			result.append(phonemes.CONS_D)
		elif l == 'e':
			result.append(phonemes.VOWEL_E)
		elif l == 'f':
			result.append(phonemes.CONS_F)
		elif l == 'g':
			result.append(phonemes.CONS_G)
		elif l == 'h':
			result.append(phonemes.CONS_H)
		elif l == 'i':
			result.append(phonemes.VOWEL_I)
		elif l == 'j':
			result.append(phonemes.CONS_J)
		elif l == 'k':
			result.append(phonemes.CONS_K)
		elif l == 'l':
			result.append(phonemes.CONS_L)
		elif l == 'm':
			result.append(phonemes.CONS_M)
		elif l == 'n':
			result.append(phonemes.CONS_N)
		elif l == 'o':
			result.append(phonemes.VOWEL_O)
		elif l == 'p':
			result.append(phonemes.CONS_P)
		elif l == 'q':
			result.append(phonemes.CONS_K) # super primitive!
		elif l == 'r':
			result.append(phonemes.CONS_R)
		elif l == 's':
			result.append(phonemes.CONS_S)
		elif l == 't':
			result.append(phonemes.CONS_T)
		elif l == 'u':
			result.append(phonemes.VOWEL_U)
		elif l == 'v':
			result.append(phonemes.CONS_V)
		elif l == 'w':
			result.append(phonemes.CONS_W)
		elif l == 'x':
			result.append(phonemes.CONS_K)
			result.append(phonemes.CONS_S)
		elif l == 'y':
			result.append(phonemes.CONS_Y)
		elif l == 'z':
			result.append(phonemes.CONS_Z)
		elif l == '.':
			result.append(phonemes.PUNC_PERIOD)
		elif l == ',' or l == ';':
			result.append(phonemes.PUNC_COMMA)
		elif l == '!':
			result.append(phonemes.PUNC_EXCLAIM)
		elif l == '?':
			result.append(phonemes.PUNC_QUESTION)
		else:
			pass # default case

	return result