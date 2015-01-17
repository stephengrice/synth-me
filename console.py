import tts

if __name__ == "__main__":
	message = input("Message: ")
	tts.text_to_speech(message, debug=True)