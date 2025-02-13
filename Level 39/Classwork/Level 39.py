# 1) Generate range of integers
def generate_range(min, max, step):
    num=[]
    for i in range(min,max+1,step):
       num.append(i)
    return num
# 2) reverseIt
def reverse_it(data):
    if type(data) in [int, str, float]:
        return type(data)(str(data)[::-1])
    return data
# 3) Sun without highest and lowest number
def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr else 0
# 4) Count by X
def count_by(x, n):
    arr = []
    for num in range(1, n+1):
        result = x * num
        arr.append(result)
    return arr
