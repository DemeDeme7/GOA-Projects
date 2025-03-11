# 1) ✅
# 2) შემენით tuple, რომელშიც შეინახავთ საყიდლების სიას და მოახდინეთ მათი unpacking (დაშლა),რათა მიანიჭოთ თითოეული ელემენტი ცალკეულ ცვლადებს და დაბეჭდეთ ეს ცვლადები.შემენით tuple, რომელშიც შეინახავთ საყიდლების სიას და მოახდინეთ მათი unpacking (დაშლა),რათა მიანიჭოთ თითოეული ელემენტი ცალკეულ ცვლადებს და დაბეჭდეთ ეს ცვლადები.


shopping_list = ("Apple", "Orange", "Banana", "Milk", "Bread")
(item1, item2, item3, item4, item5) = shopping_list
print(item1)
print(item2)
print(item3)
print(item4)
print(item5)
# 3) შექმენით tuple და შეინახეთ Fast food პროდუქტები. შემდეგ შეცვალეთ ეს tuple და მათში ჩაამატეთ ჯანსაღი საკვები პროდუქტები.
# tuple-ები არ იცვლება
# მეორე გზა:
fast_food = ("Burger", "Pizza", "Fries", "Hot Dog", "Fried Chicken")
healthy_food = ("Salad", "Fruit")
new_menu = fast_food + healthy_food
print(new_menu)
# 4) კომენტარის სახით ახსენით, თუ რა ფუნქციას ასრულებს Asterisk და როგორ აღინიშნება ის.
# Asterisk აღინიშნება "*" სიმბოლოთი, ის საშუალებას გვაძლევს რომ შევინახოთ რამდენიმე tuple-ის ელემენტი ერთ ცვლადში

#5) მოცემულია შემდეგნაირი tuple:
# months = ("January", "February", "March", "April", "May")
# (first, second, third, fourth*)= months

# რას გამოიტანს მოცემული კოდი?
# print(first)
# print(second)
# print(third)
# print(fourth)
# ერორს, რადგან Asterisk-ი უნდა ეწეროს ცვლადის წინ.

# გასწორებული კოდი:
months = ("January", "February", "March", "April", "May")

# რას გამოიტანს მოცემული კოდი?
(first, second, third, *fourth) = months

print(first)   # January
print(second)  # February
print(third)   # March
print(fourth)  # ['April', 'May']











