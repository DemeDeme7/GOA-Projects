# 1)
def format_money(amount):
    return '$%0.2f' % amount
# 2)
def swap_values(args): 
    args[0], args[1] = args[1], args[0]
    return args
# 3)
def same_case(a, b):
    return a.isupper() == b.isupper() if a.isalpha() and b.isalpha() else -1
# 4)
def sum_mul(n, m):
    if not (n > 0 and m > 0):
        return "INVALID"
    return sum(range(n, m, n))
# 5)
def multiple_of_index(arr):
    li = []
    if arr[0] == 0:
            li.append(0)
    for i in range(1,len(arr)):
        if arr[i] % i == 0:
            li.append(arr[i])

    return li
# 6)
