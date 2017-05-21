# tts.py
# Pulls all three pieces together: convertwords, convertphonemes, convertsounds

DATABASE_NAME = "data/pronunciation.db"
OUTPUT_FILE = "output.wav"

from synthme import convertwords, convertphonemes, convertsounds

def text_to_speech(message, output_file=OUTPUT_FILE, debug=False, use_pronunciation_dict=True):
	debug and print("Text to Speech Generation started.")

	words = convertwords.text_to_words(message)
	debug and print("Words list: " + str(words))
	phonemes = convertphonemes.words_to_phonemes(words, use_pronunciation_dict)
	debug and print("Phonemes list: " + str(phonemes))
	convertsounds.phonemes_to_sounds(phonemes, output_file)
	debug and print("File created.")
    