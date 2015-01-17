import convertwords, convertphonemes, convertsounds

if __name__ == "__main__":
	message = input("Message: ")
	words = convertwords.text_to_words(message)
	print("Words: " + str(words))
	phonemes = convertphonemes.words_to_phonemes(words)
	print("Phonemes: " + str(phonemes))
	convertsounds.phonemes_to_sounds(phonemes)
	print("Maybe if we're lucky, there's a soundfile now.")