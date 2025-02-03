# Jaden case strings
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())
# Sum of a sequence
def sequence_sum(begin, end, step):
    if begin > end:
        return 0
    return sum(range(begin, end + 1, step))
# Regex count lowercase letters
def lowercase_count(strng):
    return sum(a.islower() for a in strng)
# How good are you really?
def better_than_average(class_points, your_points):
    average_score = sum(class_points) / len(class_points)
    return your_points > average_score
