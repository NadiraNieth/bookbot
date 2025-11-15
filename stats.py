def get_book_text (path_to_file):
    with open(path_to_file) as f:
        content = f.read()
    return content

def count_words (text):
    return len(text.split())

def count_char(text:str):
    num = {}
    text = text.lower()

    for char in text:
        if char not in num:
            num[char] = 1
        else:
            num[char] += 1
    return num