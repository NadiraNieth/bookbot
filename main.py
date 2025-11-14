def get_book_text (path_to_file):
    with open(path_to_file) as f:
        content = f.read()
    return content

def count_words (text):
    num_words = 0
    words = text.split()
    for word in words:
        num_words += 1
    return num_words

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    print (f"Found {count_words(book_text)} total words")

main()