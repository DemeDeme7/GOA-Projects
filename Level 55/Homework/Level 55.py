# 1) შექმენით dictionary სადაც შეინახავთ მინიმუმ 3 key'ს და ასევე შექმენით 2 ცარიელი სია for loop'ის დახმარებით პირველ სიაში დაამატეთ key ხოლო მეორე სიაში კი value ბოლოს კი გამოიტანეთ ერთად.
from linecache import clearcache

info = {
    "name": "Deme",
    "age": 12,
    "height": "167cm"
}

keys_list = []
values_list = []

for i in info:
    keys_list.append(i)
    values_list.append(info[i])
# 2) მოცემული გაქვთ რაიმე result ცვლადი რომელშიც შეყვანილია სია [10,43,12,11,94,10,55,7,11] თქვენი დავალებაა გააქროთ ყველა დუბლიკატი ლისტიდან „თანმიმდევრობას მნიშვნელობა არაქვს“.
result = [10, 43, 12, 11, 94, 10, 55, 7, 11]
no_duplicates = list(set(result))
print(no_duplicates)
# 3) დღევანდელ ახსნილ მეთოდებზე გააკეთეთ მაგალითები თითო მეთოდზე 5 მაგალითი მაინც.

# .update()
a = {1, 2}
a.update({3, 4})
print(a)

b = {5}
a.update(b)
print(a)

a.update([6, 7])
print(a)

a.update("47")
print(a)

a.update()
print(a)

# .union()
a = {1, 2}
b = {3, 4}
print(a.union(b))

print(a.union([5, 6]))

print(a.union("78"))

print(a.union({2, 9}))

print(a.union())

# |
a = {1, 2}
b = {3, 4}
print(a | b)

print(a | {2, 5})

print(a | set())

print(a | {6})

print({7} | {8})

# symmetric.difference()
a = {1, 2}
b = {2, 3}
print(a.symmetric_difference(b))

print(a.symmetric_difference({1, 4}))

print(a.symmetric_difference({}))

print(a.symmetric_difference([2]))

print(a.symmetric_difference("13"))

# ^
a = {1, 2}
b = {2, 3}
print(a ^ b)

print(a ^ {4})

print(a ^ set())

print(a ^ {1})

print({5} ^ {6, 5})

# .intersection()
a = {1, 2}
b = {2, 3}
print(a.intersection(b))

print(a.intersection([2]))

print(a.intersection("12"))

print(a.intersection({5}))

print(a.intersection())

# .remove()
a = {1, 2, 3}
a.remove(2)
print(a)

a.remove(3)
print(a)

a = {5}
a.remove(5)
print(a)

a = {7, 8}
a.remove(8)
print(a)

a = {9}
a.remove(9)
print(a)

# .discard()
a = {1, 2}
a.discard(2)
print(a)

a.discard(3)
print(a)

a = set()
a.discard(1)
print(a)

a = {4, 5}
a.discard(4)
print(a)

a.discard(5)
print(a)

# .clear()
a = {1, 2, 3}
a.clear()
print(a)

b = {4}
b.clear()
print(b)

c = set()
c.clear()
print(c)

d = {5, 6}
d.clear()
print(d)

e = {"a"}
e.clear()
print(e)

# del
a = {1, 2}
del a

b = {3}
del b

c = set()
del c

d = {4, 5}
del d

e = {6}
del e
# 4) შექმენით ცარიელი dictionary შემდეგ მომხმარებელს შემოატანინეთ ჯერ key  შემდეგ კი value ამის შემდეგ თხოვეთ შეცვალოს ძველი value  და შემოატანინეთ ახალი მნიშვნელობა შემდეგ კი გამოიტანეთ საბოლოო dictionary.
data = {}

key = input("Enter a key: ")
value = input("Enter a value: ")

data[key] = value

new_value = input("Enter a new value for the key '" + key + "': ")
data[key] = new_value

print("Final dictionary:", data)
# 5) შექმენით სეტის მსგავსი ფუნქცია რომელიც მიიღებს ლისტს და ლისტიდან წაშლის დუბლიკატებს „ფუნქციაში არ გამოიყენოთ სეტი“
def remove_duplicates(lst):
    unique_list = []
    for i in lst:
        if i in unique_list:
            continue
        unique_list.append(i)
    return unique_list
