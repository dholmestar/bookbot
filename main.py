from stats import get_word_count, get_char_count, sort_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    story_text = get_book_text(sys.argv[1])
    sorted_dict = sort_dict(get_char_count(story_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(story_text)} total words")
    print("--------- Character Count -------")
    for dictionary in sorted_dict:
        char = dictionary["char"]
        count = dictionary["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
    

def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

main()