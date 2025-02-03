# Function 1-hello world
def greet():
    return "hello world!"
# Opposite number
def opposite(number):
    return -number
# Return Negative
def make_negative(number):
    if number > 0:
        return -number
    return number
# Sum of positive
def positive_sum(arr):
    total = 0
    for number in arr:
        if number > 0:
            total += number
    return total
# String Repeat
def repeat_str(repeat, string):
    return string * repeat
