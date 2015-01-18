import phonemes, sqlite3, ast, re

def words_to_phonemes(words, c, use_pronunciation_dict=True):
	# Takes list of words and punctuation

	result = []
	for word in words:
		# Check if the word has been learned
		row = False
		if use_pronunciation_dict:
			c.execute("SELECT * FROM main WHERE word=?", (word,))
			row = c.fetchone()
		if row:
			# Convert phoneme list to python list; return
			result.extend(ast.literal_eval(row['phoneme_list']))
		else:
			# If not recognized, take an (un)educated guess
			blocked = phoneme_scan(word)
			result.extend(phoneme_blocks_to_list(blocked))
		result.append(phonemes.PAUSE_WORD)
	return result

def phoneme_blocks_to_list(blocks):
	blocks_list = re.findall("\[\d+\]", blocks)
	result = []
	for b in blocks_list:
		result.append(int(re.sub(r'\[(\d+)\]', r'\1', b)))
	return result


def phoneme_scan(word):
	while re.search("[a-zA-Z.,;!\?]", word): # Keep replacing letters with phonemes in brackets [] until there are no more letters
		# Special patterns
		word = replace_with_phoneme(word, r'iew', (phonemes.CONS_Y, phonemes.VOWEL_OO,phonemes.CONS_W))
		
		word = replace_with_phoneme(word, r'oo', (phonemes.VOWEL_OO,))
		word = replace_with_phoneme(word, r'ou', (phonemes.VOWEL_OO,))
		word = replace_with_phoneme(word, r'ea', (phonemes.VOWEL_II,))
		word = replace_with_phoneme(word, r'ee', (phonemes.VOWEL_II,))

		word = replace_with_phoneme(word, r'gg', (phonemes.CONS_J,))
		word = replace_with_phoneme(word, r'dd', (phonemes.CONS_D,))
		word = replace_with_phoneme(word, r'ph', (phonemes.CONS_F,))
		word = replace_with_phoneme(word, r'll', (phonemes.CONS_L,))
		word = replace_with_phoneme(word, r'ss', (phonemes.CONS_S,))
		word = replace_with_phoneme(word, r'nn', (phonemes.CONS_N,))
		word = replace_with_phoneme(word, r'ch', (phonemes.CONS_CH,))
		word = replace_with_phoneme(word, r'sh', (phonemes.CONS_SH,))
		word = replace_with_phoneme(word, r'th', (phonemes.CONS_TH,))
		word = replace_with_phoneme(word, r'ck', (phonemes.CONS_K,))

		# Default letters
		word = replace_with_phoneme(word, "a", (phonemes.VOWEL_A,))
		word = replace_with_phoneme(word, "b", (phonemes.CONS_B,))
		word = replace_with_phoneme(word, "c", (phonemes.CONS_K,))
		word = replace_with_phoneme(word, "d", (phonemes.CONS_D,))
		word = replace_with_phoneme(word, "e", (phonemes.VOWEL_E,))
		word = replace_with_phoneme(word, "f", (phonemes.CONS_F,))
		word = replace_with_phoneme(word, "g", (phonemes.CONS_G,))
		word = replace_with_phoneme(word, "h", (phonemes.CONS_H,))
		word = replace_with_phoneme(word, "i", (phonemes.VOWEL_I,))
		word = replace_with_phoneme(word, "j", (phonemes.CONS_J,))
		word = replace_with_phoneme(word, "k", (phonemes.CONS_K,))
		word = replace_with_phoneme(word, "l", (phonemes.CONS_L,))
		word = replace_with_phoneme(word, "m", (phonemes.CONS_M,))
		word = replace_with_phoneme(word, "n", (phonemes.CONS_N,))
		word = replace_with_phoneme(word, "o", (phonemes.VOWEL_O,))
		word = replace_with_phoneme(word, "p", (phonemes.CONS_P,))
		word = replace_with_phoneme(word, "q", (phonemes.CONS_K,))
		word = replace_with_phoneme(word, "r", (phonemes.CONS_R,))
		word = replace_with_phoneme(word, "s", (phonemes.CONS_S,))
		word = replace_with_phoneme(word, "t", (phonemes.CONS_T,))
		word = replace_with_phoneme(word, "u", (phonemes.VOWEL_U,))
		word = replace_with_phoneme(word, "v", (phonemes.CONS_V,))
		word = replace_with_phoneme(word, "w", (phonemes.CONS_W,))
		word = replace_with_phoneme(word, "x", (phonemes.CONS_K, phonemes.CONS_S))
		word = replace_with_phoneme(word, "y", (phonemes.CONS_Y,))
		word = replace_with_phoneme(word, "z", (phonemes.CONS_Z,))
		word = replace_with_phoneme(word, ".", (phonemes.PUNC_PERIOD,))
		word = replace_with_phoneme(word, ",", (phonemes.PUNC_COMMA,))
		word = replace_with_phoneme(word, ";", (phonemes.PUNC_COMMA,))
		word = replace_with_phoneme(word, "!", (phonemes.PUNC_EXCLAIM,))
	return word

def replace_with_phoneme(word, letters, phoneme_ids):
	result = ""
	for phoneme_id in phoneme_ids:
		result += "["+str(phoneme_id)+"]"
	return word.replace(letters, result)