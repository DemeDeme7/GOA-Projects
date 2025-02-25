# 1)
def expression_matter(a, b, c):
    if 1 not in [a, b, c]:
        return a * b * c
    elif a == 1 and c == 1:
        return a + b + c
    elif a == 1 or (b == 1 and a < c):
        return (a + b) * c
    else:
        return a * (b + c)
# 2)
# ?
# 3)
def spin_words(sentence):
    words = sentence.split()
    result = []
    for word in words:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)

    return " ".join(result) 
# 4)
def solve(s):
    upper = 0
    lower = 0
    for char in s:
        if char.islower():
            lower += 1
        else:
            upper += 1
            
    if upper == lower or lower > upper:
        return s.lower()
    else:
        return s.upper()
# 5)
# ?
# 6)
def max_multiple(divisor, bound):
    return bound // divisor * divisor
# 7)
def alphabetic(s):
    return sorted(s) == list(s)
