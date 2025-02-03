# 1)შექმენით ფუნქცია რომელსაც გადაეცემა სია,გამოითვალეთ რიცხვების ჯამი for ციკლის საშუალებითაც და sum() ფუნქციის გამოყენებითაც აუცილებლად დააბრუნეთ შედეგი return ის გამოყენებით
def calculate_sum(numbers):
    total_for = 0
    for num in numbers:
        total_for += num
    
    total_sum = sum(numbers)
    
    return total_for, total_sum
