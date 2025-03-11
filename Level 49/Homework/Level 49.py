# 1) Take the Derivative
def derive(coefficient, exponent):
    return str(coefficient * exponent) + "x^" + str(exponent-1)
# 2) Return the day
def whatday(num):
    if num == 1:
        return "Sunday"
    elif num == 2:
        return "Monday"
    elif num == 3:
        return "Tuesday"
    elif num == 4:
        return "Wednesday"
    elif num == 5:
        return "Thursday"
    elif num == 6:
        return "Friday"
    elif num == 7:
        return 'Saturday'
    else:
        return "Wrong, please enter a number between 1 and 7"
# 3) Unfinished Loop - Bug Fixing #1
def create_array(n):
    res=[]
    i=1
    while i<=n:
        res+=[i]
        i+= 1
    return res
# 4) Leap years
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
# 5) For UFC Fans (Total Beginners): Conor McGregor vs George Saint Pierre
def quote(fighter):
    winner = fighter.lower()
    if winner == "george saint pierre":
        return "I am not impressed by your performance."
    if winner == "conor mcgregor":
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"