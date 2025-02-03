# .lower()-აპატარავებს მოცემული სტრინგის მქონე ასოებს.
# .upper()-ადიდებს მოცემული სტრინგის მქონე ასოებს.
# .capitalise()-ადიდებს მოცემული სტრინგის პირველ ასოს
# .find()-პოულობს სტრინგში მოცემულ მონაცემს ინდექსირების მეშვეობით,რომლის შემდგომ შეგვიძლია რაიმე ოპერაციის შესრულება მასზე.

user_surname = input("Please enter your surname:")
if user_surname[0] .isupper():
    print("Hello")
elif user_surname[0] .islower():
    print("Bye")


user_name = input("Please enter your name:")
character = input("Please enter a character:")

if character in user_name:
    print("Found it!")
else:
    print("Can't find the character!")

user_surname2 = input("Please enter your surname:")
choice = input("Would you like your surname's characters to be converted to capital,lowercase or only the first letter capitalised?(upper/lower/capitalise):")
if choice == "upper":
    print(user_surname2.upper())
elif choice == "lower":
    print(user_surname2.lower())
elif choice == "capitalise":
    print(user_surname2.lower())
