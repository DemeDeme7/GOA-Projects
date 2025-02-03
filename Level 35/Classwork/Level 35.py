def capitals(word):
    return [i for i, char in enumerate(word) if char.isupper()]
def max_multiple(divisor, bound):
    return bound - (bound % divisor) # გამოაქვს bound-ის(ზღვარის) ზღვარის და გამყობის(divisor) ნაშთის სხვაობა
def sum_digits(number):
    # აქცევს სტრინგს,ან სხვა მონაცემს(ინტეჯერის გარდა) ინტეჯერად
    return sum(int(digit) for digit in str(number) if digit.isdigit())