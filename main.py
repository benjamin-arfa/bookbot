from stats import get_num_words,new_function
import sys

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) < 2:
        print("python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    print(f"Analyzing book found at {book}...")
    get_num_words(book)
    new_function(book)
    print("============= END ===============")
main()
