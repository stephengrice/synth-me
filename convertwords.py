# convertwords.py
# Tokenize input
# Raw text is turned into a list of words
# TODO: Convert numerical values to words

import re

def text_to_words(data):
	return re.findall(r"[\w']+|[.,!?;]", data.lower())