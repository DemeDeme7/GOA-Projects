# 1) Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence
def replace_exclamation(st):
    vowels = "aeiouAEIOU"
    result = ""

    for i in st:
        if i in vowels:
            result += "!"
        else:
            result += i
    return result
# 2) Surface Area and Volume of a Box
def get_size(w, h, d):
    area = 2 * (w * h + h *d +w *d)
    volume = w * h * d
    return [area, volume]
# 3) Find min and max
def get_min_max(seq):
    return min(seq), max(seq)
# 4) Do you speak "English"?
def sp_eng(sentence):
    if "english" in sentence.lower():
        return True
    else:
        return False
# 5) Who ate the cookie?
def cookie(x):
    if type(x) == str:
        return "Who ate the last cookie? It was Zach!"
    elif type(x) == int or type(x) == float:
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"
    