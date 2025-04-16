from stats import count_words, count_characters, list_of_dictionaries, sort_on,  sorting
import sys
if len(sys.argv) != 2:
	print ("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
def get_book_text(filepath):
        with open(filepath) as f:
                file_contents = f.read()
        return file_contents
def main():
	print(f"============ BOOKBOT ============ \n Analyzing book found at {sys.argv[1]} \n----------- Word Count ----------")
	booktext = get_book_text(sys.argv[1])
	num_words = count_words(booktext)
	print(f" Found {num_words} total words")
	print("--------- Character Count -------")
	dict_character_count = count_characters(booktext)
	list_of_dictionaries(dict_character_count)
	sorted_dic = sorting(dict_character_count)
	filtered_characters = [d for d in sorted_dic if d["char"].isalpha()]
	for d in filtered_characters:
		print(f' {d["char"]}: {d["count"]}')
	print("============= END ===============")
main()
