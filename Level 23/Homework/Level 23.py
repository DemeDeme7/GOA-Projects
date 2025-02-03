# 1) მომხმარებელს შემოატანინეთ მისი სახელი დიდი ასოებით და შეინახეთ ცვლადში სახელად name და .lower() ფუნქციის მეშვეობით გადააქციეთ ცვლადის მნიშვნელობა  პატარა ასოებად. 
username = input("Please enter your name in capital letters:")
print(username.lower())

# 2) ცვლადში შეინახეთ თქვენი გვარი პატარა ასოებით, შემდეგ .upper() ფუნქციის მეშვეობით გადააქციეთ ცვლადის მნიშვნელობა  დიდ ასოებად.
surname = "chulukhadze"
print(surname.upper())

# 3) ცვლადში შეინახეთ სტრინგი პატარა ასოებით, შემდეგ .capitalize() ფუნქციის მეშვეობით გადააქციე პირველი ასო დიდ ასოდ.
string = "goa"
print(string.capitalize())
# 4)ცვლადში შეინახეთ რაიმე სტრინგი,შემდეგ find() ფუნქციის მეშვეობით იპოვეთ რომელ ინდექსზეა კონკრეტული ასო
string_2 = "Hello"
target_character = "l"
index = string_2.find(target_character)
if index == True:
    print("Your character was found in the string!:", target_character)
if index == False:
    print("Your character wasn't found in the string!:", target_character)

# 5)შექმენით სია სტრინგით და თითოეული სტრინგი გადაიყვანეთ დიდ ასოებად for ციკლის მეშვეობით
list = ["hello", "good morning", "good evening", "good night",]
for index in list:
    print(index.upper())
    