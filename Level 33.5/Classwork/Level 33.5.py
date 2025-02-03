
def maskify(cc):
    if len(cc) <= 4:
        return cc
    return '#' * (len(cc) - 4) + cc[-4:]

def solution(text, ending):
    return text.endswith(ending)

def capitals(word):
    return [i for i, char in enumerate(word) if char.isupper()]