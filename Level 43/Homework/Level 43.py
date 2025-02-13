# Sum of a sequence
def sequence_sum(begin, end, step):
    if begin > end:
        return 0
    return sum(range(begin, end + 1, step))
# List filtering
def filter_list(l):
    new_list =[]
    for x in l:
        if type(x) != str:
            new_list.append(x)
    return new_list
# Jaden Casing Strings
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())
# Sum Mixed Array
def sum_mix(arr):
    return sum(map(int, arr))
# Array plus array
def array_plus_array(arr1,arr2):
    return sum(arr1+arr2)
# Reversed Words
def reverseWords(str):
    return ' '.join(reversed(str.split(' ')))
# Sum The Strings
def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))