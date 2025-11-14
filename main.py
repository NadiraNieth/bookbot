def get_book_text (path_to_file):
    with open(path_to_file) as f:
        content = f.read()
    return content

def count_words (text):
    return len(text.split())

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    print (f"Found {count_words(book_text)} total words")

main()