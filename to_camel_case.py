
def the_camel_case(text):

	if text[0].isupper():
		if '-' in text:
			phrase = text.replace('-', ' ').title()
			last_phrase = phrase.replace(' ', '')
			print(last_phrase)

		elif '_' in text:
			phrase = text.replace('_', ' ').title()
			last_phrase = phrase.replace(' ', '')
			print(last_phrase)

	elif text[0].islower():
		if '-' in text:
			phrase = text.replace('-', ' ').title()
			phrase_1 = phrase.replace(' ', '')
			phrase_2 = phrase_1[0].lower()
			phrase_3 = phrase_1[1:]
			last_phrase = phrase_2 + phrase_3
			print(last_phrase)

		elif '_' in text:
			phrase = text.replace('_', ' ').title()
			phrase_1 = phrase.replace(' ', '')
			phrase_2 = phrase_1[0].lower()
			phrase_3 = phrase_1[1:]
			last_phrase = phrase_2 + phrase_3
			print(last_phrase)

the_camel_case('The-algerian-warrior')












