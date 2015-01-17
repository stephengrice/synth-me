import wave, phonemes, os

VOICE_PATH = os.path.dirname(__file__) + "/voices/steve/"

def phonemes_to_sounds(phoneme_list):
	infiles = []
	outfile = "output.wav"
	for phoneme in phoneme_list:
		infiles.append(get_sound_file(phoneme))
	data = []
	for infile in infiles:
		w = wave.open(infile, 'rb')
		data.append( [w.getparams(), w.readframes(w.getnframes())] )
		w.close()

	output = wave.open(outfile, 'wb')
	output.setparams(data[0][0])
	output.writeframes(data[0][1])
	output.writeframes(data[1][1])
	output.close()

def get_sound_file(phoneme):
	fname = "%02d" % phoneme
	return VOICE_PATH + fname + ".wav"