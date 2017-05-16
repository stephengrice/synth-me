# tts.py
# Pulls all three pieces together: convertwords, convertphonemes, convertsounds

DATABASE_NAME = "data/pronunciation.db"
OUTPUT_FILE = "output.wav"

from synthme import convertwords, convertphonemes, convertsounds
import sqlite3

def text_to_speech(message, output_file=OUTPUT_FILE, debug=False, use_pronunciation_dict=True):
	debug and print("Text to Speech Generation started.")

	debug and print("Opening database connection.")
	conn = get_connection()
	c = conn.cursor()

	words = convertwords.text_to_words(message)
	debug and print("Words list: " + str(words))
	phonemes = convertphonemes.words_to_phonemes(words, c, use_pronunciation_dict)
	debug and print("Phonemes list: " + str(phonemes))
	convertsounds.phonemes_to_sounds(phonemes, output_file)
	debug and print("File created.")

	conn.close()
	debug and print("Database connection closed.")

def get_connection():
	conn = sqlite3.connect(DATABASE_NAME)
	conn.row_factory = sqlite3.Row
	return conn
  