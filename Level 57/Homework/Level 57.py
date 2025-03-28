# 1) Thinkful - Logic Drills: Traffic light
def update_light(current):
    if current is "green":
        return "yellow"
    if current is "yellow":
        return "red"
    if current is "red":
        return "green"
# 2) Count by X
def count_by(x, n):
    arr = []
    for num in range(1, n + 1):
        result = x * num
        arr.append(result)
    return arr
# 3) Abbreviate a Two Word Name
def abbrev_name(name):
    parts = name.split()
    return parts[0][0].upper() + "." + parts[1][0].upper()
# 4) Count of positives / Sum of negatives
def count_positives_sum_negatives(arr):
    if not arr:
        return []

    count_pos = 0
    sum_neg = 0

    for num in arr:
        if num > 0:
            count_pos += 1
        elif num < 0:
            sum_neg += num

    return [count_pos, sum_neg]
