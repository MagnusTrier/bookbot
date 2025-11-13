from stats import get_word_count, get_char_count, sorted_list
import sys

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    get_book_text(sys.argv[1])

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
        num_words = get_word_count(contents) 
        char_count = get_char_count(contents)


    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    sorted = sorted_list(char_count)
    for i in sorted:
        print(f'{i['char']}: {i['num']}')
    print('============= END ===============')

main()


