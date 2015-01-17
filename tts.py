import convertwords, convertphonemes, convertsounds

OUTPUT_FILE = "output.wav"

def text_to_speech(message, debug=False, output_file=OUTPUT_FILE):
	debug and print("Text to Speech Generation started.")
	words = convertwords.text_to_words(message)
	debug and print("Words list: " + str(words))
	phonemes = convertphonemes.words_to_phonemes(words)
	debug and print("Phonemes list: " + str(phonemes))
	convertsounds.phonemes_to_sounds(phonemes, output_file)
	debug and print("File created.")