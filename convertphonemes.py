import phonemes, sqlite3, ast, re

def words_to_phonemes(words, c):
	# Takes list of words and punctuation

	result = []
	for word in words:
		# Check if the word has been learned
		c.execute("SELECT * FROM main WHERE word=?", (word,))
		row = c.fetchone()
		if row:
			# Convert phoneme list to python list; return
			result.extend(ast.literal_eval(row['phoneme_list']))
		else:
			# If not recognized, take an (un)educated guess
			for letter in word:
				result.append(guess_phoneme(letter))
		result.append(phonemes.PAUSE_WORD)
	return result

def phoneme_scan(word):
	while re.search("[a-zA-Z]", word): # Keep replacing letters with phonemes in brackets [] until there are no more letters
		word = replace_with_phoneme(word, "oo", phonemes.VOWEL_OO)
		# do this until no letters haven't been checked

def replace_with_phoneme(word, letters, phoneme_id):
	result = "["+str(phoneme_id)+"]"
	return word.replace(letters, result)

def guess_phoneme(letter):
	l = letter.lower()
	if l == 'a':
		return phonemes.VOWEL_A
	elif l == 'b':
		return phonemes.CONS_B
	elif l == 'c':
		return phonemes.CONS_K
	elif l == 'd':
		return phonemes.CONS_D
	elif l == 'e':
		return phonemes.VOWEL_E
	elif l == 'f':
		return phonemes.CONS_F
	elif l == 'g':
		return phonemes.CONS_G
	elif l == 'h':
		return phonemes.CONS_H
	elif l == 'i':
		return phonemes.VOWEL_I
	elif l == 'j':
		return phonemes.CONS_J
	elif l == 'k':
		return phonemes.CONS_K
	elif l == 'l':
		return phonemes.CONS_L
	elif l == 'm':
		return phonemes.CONS_M
	elif l == 'n':
		return phonemes.CONS_N
	elif l == 'o':
		return phonemes.VOWEL_O
	elif l == 'p':
		return phonemes.CONS_P
	elif l == 'q':
		return phonemes.CONS_K # super primitive!
	elif l == 'r':
		return phonemes.CONS_R
	elif l == 's':
		return phonemes.CONS_S
	elif l == 't':
		return phonemes.CONS_T
	elif l == 'u':
		return phonemes.VOWEL_U
	elif l == 'v':
		return phonemes.CONS_V
	elif l == 'w':
		return phonemes.CONS_W
	elif l == 'x':
		return phonemes.CONS_Z
	elif l == 'y':
		return phonemes.CONS_Y
	elif l == 'z':
		return phonemes.CONS_Z
	elif l == '.':
		return phonemes.PUNC_PERIOD
	elif l == ',' or l == ';':
		return phonemes.PUNC_COMMA
	elif l == '!':
		return phonemes.PUNC_EXCLAIM
	elif l == '?':
		return phonemes.PUNC_QUESTION
	else:
		return phonemes.PAUSE_WORD

