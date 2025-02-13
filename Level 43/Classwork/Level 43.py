# 1)
def nth_even(n):
    return n * 2 - 2
# 2)
def add_length(str_):
    list = []
    for i in str_.split():
        list.append(i + ' ' + str(len(i)))
    return list
# 3)
# To square(root) or not to square(root)
def square_or_square_root(arr):
    result = []
    for x in arr:
        root = x**0.5
        if root.is_integer():
            result.append(root)
        else:
            result.append(x*x)
    return result
# 4)
# Remove First and Last Character Part Two
def array(string):
  res = ' '.join(string.split(',')[1:-1])
  if len(res) > 0:
      return res
  else:
    None
# 5) 
# Different volumes of cuboids
# ?
