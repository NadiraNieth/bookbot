from stats import get_book_text, count_words, count_char, sort_dic



def main():
    book_path ="./books/frankenstein.txt"
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