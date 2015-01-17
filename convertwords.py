import re

def text_to_words(data):
	return re.findall(r"[\w']+|[.,!?;]", data.lower())