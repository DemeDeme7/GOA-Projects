# 8KYU
# Opposite number
def opposite(n):
    return -n
# Count of positives
def count_positives_sum_negatives(arr):
    pos_count = sum(1 for x in arr if x > 0)
    neg_sum = sum(x for x in arr if x < 0)
    return [pos_count, neg_sum]
# Are you playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"Yes, {name} plays banjo"
    return f"No, {name} doesn't play banjo"
# 7KYU
# Convert boolean values to strings
def bool_to_word(b):
    return "Yes" if b else "No"
# Sum of positives
def positive_sum(arr):
    return sum(i for i in arr if i > 0)
# 6KYU
# String ends with?
def solution(string, ending):
    return string.endswith(ending)
