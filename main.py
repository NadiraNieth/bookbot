from stats import get_book_text
from stats import count_words
from stats import count_char

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    number_of_chars = count_char(book_text)
    print (f"Found {count_words(book_text)} total words")
    print(number_of_chars)

main()