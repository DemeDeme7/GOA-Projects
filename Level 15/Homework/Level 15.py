# 1)
selfname = "Demetre"
username = input("Please enter your name:")
if selfname == username:
    print("Hello")
else:
    print("Bye")
# 2)
favnumber = 7
userfavnumber = int(input("Please enter your favourite number:"))
if favnumber == userfavnumber:
    print("Perfect")
elif userfavnumber > favnumber:
    print("More")
else:
    print("Less")
# 3)    
for num in range(150):
    if num % 2 == 0:
        print("Luwia", num)
    else:
        print("Kentia", num)
# 4)
ownage = 12
userage = int(input("Please enter your age:"))
# (მომხმარებელს და მე ჩვენი სახელები უკვე დეკლარირებული გვქონდა,ხაზი 2 და 3.)
if userage == ownage and username == selfname:
    print("Twins")
else:
    print("Not Twins")
# 5)
account_password = "Qwerty"
userinput = ""
while userinput != account_password:
    userinput = input("Please enter your password:")
print("Access granted!")
#                                                               -end of homework-
