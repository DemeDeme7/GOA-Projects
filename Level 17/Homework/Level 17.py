# 1)
groceries = ["apple", "banana", "cherry", "pear", "pineapple"]
for i in range(len(groceries)):
    print(groceries[i])
# 2)
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(elements)):
    print(elements[i])

for element in elements:
    print(element)
# 3)
numbers = [3, 8, 34, 15, 9, 43, 20, 72]
for i in numbers:
    if i > 10:
        print(i)
# 4)
elements_2 = ["hi", "david", 3.14 , "GOA", 17 , True , False]
for i in elements_2:
    print(type(i))