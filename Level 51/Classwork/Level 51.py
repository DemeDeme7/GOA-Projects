# 1. კომენტარის სახით ახსენით, თუ რა განასხვავებს tuple-ებს List-ებისგან.
# 1) სიები არის ცვალებადი, ე.ი. ჩვენ შეგვიძლია სიის ელემენტის შეცვლა, ხოლო tuple-ებში არ შეგვიძლია
# 2) სინტაქსი: სიები იწერება კვადრატულ ფრჩხილებში ([]), tuple-ები იწერება ჩვოულებრივ ფრჩხილებში(())

# 2. შექმენით tuple, რომელიც შეიცავს თქვენს 5 საყვარელ ფილმს, შემდეგ კი დაბეჭდეთ პირველი და ბოლო ელემენტი ამ tuple-დან.
films = ("Fight Club", "Flight Risk", "Cars", "Harry Potter", "Titanic")
print(films[0])
print(films[-1])

# 3. შემენით Tuple, რომელშიც შეინახავთ კვირის დღეებს და მოახდინეთ მათი unpacking (destruction),რათა მიანიჭოთ თითოეული ელემენტი ცალკეულ ცვლადებს და დაბეჭდეთ ეს ცვლადები.
week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

monday, tuesday, wednesday, thursday, friday, saturday, sunday = week_days

print(monday)
print(thursday)
print(saturday)
# 4. შექმენით tuple, რომელიც შეიცავს რამდენიმე ელემენტს. შემდეგ შეამოწმეთ, შეიცავს თუ არა ეს tuple კონკრეტულ ელემენტს
tuple = (10, 20, 30, 40, 50)
find = 30
if find in tuple:
    print(True)
else:
    print(False)

# 5. მოცემულია:
tuple = ("banana", "cherry", "strawberry", "raspberry")
(first, *second, third) = tuple

# რას გამოიტანს შემდეგი კოდი?
print(first)
print(second)
print(third)
