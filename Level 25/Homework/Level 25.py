# 1)შექმენით ცარიელი სია და for ციკლის მეშვეობით ჩაამატეთ ყველა ლუწი რიცხვი 0დან 200მდე, ბოლოს დაბეჭდეთ სია.
numbers = []
for number in range(0, 201):
    if number % 2 == 0:
        numbers.append(number)

print(numbers)

# 2)შექმენით ცარიელი სია და for ციკლის მეშვოებით მომხმარებელს შეეკითხეთ მისი top 5 საყვარელი სახელი (ანუ ხუთჯერ input).
namesl=[]
for i in range(5):
    names = input("Enter your favourite name:")
    namesl.append(names)
print(namesl)
# 3)შექმენით სია 10 ელემენტით და გამოიტანეთ მხოლოდ კენტ ინდექსზე მდგომი ელემენტები.
list=["h", "e", "l" ,"l", "o", 1, 2, 3, 4, 5.0]
for i in range(len(list)):
    if i % 2 == 1:
        print(list[i])
# 4)შექმენით ცვლადი რომელშიც შენახული იქნება სტრინგი შემდეგ კი გაიგეთ ამ სტრინგის სიმბოლოების რაოდენობა.
string = "lorem"
string_len = (len(string))
print(string_len)
# 5)შექმენით სია შემდგარი 5 ელემენტისგან, მომხმარებელს შემოატანინეთ რიცხვი და სიიდან ამოაგდეთ შემოტანილ რიცხვის ინდექსზე მდგომი ელემენტი.
list_2 = ["Hello", 5, 7.2, "GOA", 2]
print(list_2)
user_choice = int(input("Choose the index you want to remove from the list above(0-4):"))
if 0 <= user_choice < len(list_2):
    list_2.pop(user_choice)
    print("Updated list:", list_2)
elif user_choice > 4:
    print("Error: Please input integers(numebrs) from 0 to 4!")
elif user_choice != int():
    print("Error: Invalid syntax, Make sure to only input integers(numbers)!")
else:
    print("Unknown error")
# 6)შექმენით სია და დაბეჭდეთ ამ სიის სიგრძე.
print("The lengh of the list is:",len(list),"characters.")
