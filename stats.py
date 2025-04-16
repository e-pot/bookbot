def count_words(text):
        words = text.split()
        return len(words)
def count_characters(text):
	characters_count = {}
	for letter in text:
		lowercase_letter =  letter.lower()
		if lowercase_letter in characters_count:
			characters_count[lowercase_letter] += 1
		else:
			characters_count[lowercase_letter] = 1
	return characters_count
def list_of_dictionaries(dictionary):
	list_dicts =[]
	for pair in dictionary:
		dict ={"char" : pair, "count" : dictionary[pair]}
		list_dicts.append(dict)
	return list_dicts
def sort_on(dict):
	return dict["count"]

def sorting(dictionary):
	dictionaries = list_of_dictionaries(dictionary)
	dictionaries.sort( reverse = True, key = sort_on)
	return dictionaries
