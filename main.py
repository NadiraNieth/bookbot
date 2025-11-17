from stats import get_book_text, count_words, count_char, sort_dic
import sys


def main():
    try:
        sys.argv[1] == None
    except Exception as e:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    number_of_chars = count_char(book_text)
    sorted_list = sort_dic(number_of_chars)
    
    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    for dic in sorted_list:
        if dic["char"].isalpha():
            print(f"{dic["char"]}: {dic["num"]}")
    print("============= END ===============")

main()