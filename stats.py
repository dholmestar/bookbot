def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    text_dict = {}
    for char in text:
        char = char.lower()
        if char in text_dict:
            text_dict[char] = text_dict[char] + 1
        else:
            text_dict[char] = 1   
    return text_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dictionary):
    dict_list = []
    for key, value in dictionary.items():
        dict_list.append({"char": key, "num": value})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
