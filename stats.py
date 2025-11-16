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

def sort_on(items):
    return items["num"]

def sort_dic(dic_char):
    dic_list = []
    for key in dic_char:
        new_dic = {}
        new_dic["char"] = key
        new_dic["num"] = dic_char[key]
        dic_list.append(new_dic)
    dic_list.sort(reverse=True, key=sort_on)
    return dic_list