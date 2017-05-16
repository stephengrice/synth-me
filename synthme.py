# console.py
# Interface for TTS engine
# Interacts solely with main tts module

from synthme import tts

if __name__ == "__main__":
	message = input("Message: ")
	tts.text_to_speech(message, debug=True, use_pronunciation_dict=True)