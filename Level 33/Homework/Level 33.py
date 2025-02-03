# You Can't Code Under Preasure #1
def double_integer(i):
    return i * 2
# Friend or Foe?
def friend(x):
    #Code
    names = []
    for name in x:
        if len(name) == 4:
            names.append(name)
    return names
# Beginner - Reduce but grow
def grow(arr):
	product = 1
	for i in arr:
		product *= i
	return product
# Calculate Average
def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
# Messi goals function
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga+copaDelRey+championsLeague
# Double Char
def double_char(s):
    result = ''
    for char in s:
        result += char * 2
    return result
# Remove anchor from URL
def remove_url_anchor(url):
  return url.split('#')[0]
# Sum of Cubes
# ?

# 1)შექმენით სია, სადაც გექნებათ 5 ელემენტი. წაშალეთ სიის მე-3 ელემენტი და დაამატეთ ახალი მე-0 ინდექსზე. საბოლოოდ დააბრუნეთ ეს სია
list = [10, 20, 30, 40, 50]
list.pop(2)
list.insert(0, 5)
print(list)
# 2)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა ორი რიცხვი შემდეგ ,პირველი რიცხვი აიყვანეთ მეორე რიცხვის ხარისხში და დააბრუნეთ
def power(num1, num2):
    return num1 ** num2
# 3)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა სია შემდეგ უნდა შეამოწმოთ ამ სიის სიგრძე თუ ლუწია დააბრუნეთ --> List length is even, ხოლო სხვა შემთხვევაში დააბრუნეთ --> List length is odd
if len(list) / 2 == 0:
    print("List lenght is even")
if len(list) / 2 != 0:
    print("List lenght is odd")
    