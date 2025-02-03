# 1)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა ორი რიცხვი შემდეგ კი გამოიტანეთ ამ რიცხვების ჯამი.
num1 = 6
num2 = 2
def sum():
    print(num1 + num2)
# 2)შექმენით ფუნქცია რომელსაც გადაეცემა არგუმენტად რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ლუწია ეს რიცხვი თუ კენტი.
def check(number):
    if number % 2 == 0:
        print("The number", "⟨", num, "⟩", "is Even.")
    else:
        print("The number", "⟨", num, "⟩", "is Odd.")
num = int(input("Please enter a number(Integers only!):"))
result = check(num)

# 3)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ეს რიცხვი დადებითია თუ უარყოფითი.
def check_pos_neg(number1):
    if number1 > 0:
        print("The number", "⟨", num1, "⟩", "is Positive.")
    elif number1 < 0:
        print("The number", "⟨", num1, "⟩", "is Negative.")
    elif number1 == 0:
        print("The number", "⟨", num1, "⟩", "is Not positive, nor negative.")
num1 = int(input("Please enter a number(Integers only!):"))
result1 = check_pos_neg(num1)
# 4)შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა სახელი და დაბეჭდავს მისთვის მიესალმებას (მაგალითად: "Hello Giorgi"). გამოძახეთ ეს ფუნქცია 2-ჯერ და გადაეცით სხვადასხვა სახელი.
def greet(name):
    print("Hello",name)
greet("Deme")
greet("David")
# 5)შექმენით ფუნქცია, რომელიც იღებს ორ სტრინგს და მოახდინეთ კონკატენაცია.
def str_con(str1, str2):
    print(str1 + str2)
output = str_con("Hello", "World!")
print(output)