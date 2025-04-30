from stats import *
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    path = sys.argv[1] 
    book_text = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"{get_num_words(book_text)}")
    print("----------- Word Count ---------")     
    character_count = sort_character_count(get_character_count(book_text))
    for k, c in character_count.items():
        if k.isalpha():
            print(f"{k}: {c}")
    print("============= END ===============")

if __name__ == "__main__":
    main()


