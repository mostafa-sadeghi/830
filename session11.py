# running = True
# while running == True:
#     print("player is enjoying the game ...")
#     if input("Do you want to Continue? (y/n) ") == "n":
#         running = False
# print("Good luck!!!")

# def my_function(name):
#     print("hello", name)
#     print("welcome to python class.")
#     print("we are going to learn everythings a bout python")


# my_function("artin")
# my_function("armin")
# my_function("sara")
# my_function("taha")

# def is_even_or_odd(number):
#     if number % 2 == 0:
#         return "even"
#     else:
#         return "odd"


# print(is_even_or_odd(12))
# print(is_even_or_odd(123))
# print(is_even_or_odd(1234))


# TODO
# تابعی بنویسید که طول و عرض چهارگوش را بگیرد و مساخت و محیط ان را محاسبه نماید


# TODO
"""
یک تابع بنویسید که یک عدد بگیرد
اگر دورقم آخر آن 11، 12 یا 13 باشد
پسوند th را 
به عدد اضافه کند
512th
12th

اگر رقم یکان آن 1 باشد
st را 
به آخر آن اضافه کند

51st
1st

اگر رقم یکان آن 2 باشد
nd را به آخر آن اضافه کند

52nd
2nd
اگر رقم آخر آن 3 باشد
rd 
3rd
53rd

و برای سایر اعداد
th
را اضافه نماید

9999th

"""


# def my_function(number):
#     if number % 100 == 11 or number % 100 == 12 or number % 100 == 13:
#         return str(number) + "th"

#     if number % 10 == 1:
#         return str(number) + "st"

#     if number % 10 == 2:
#         return str(number) + "nd"

#     if number % 10 == 3:
#         return str(number) + "rd"

#     return str(number) + "th"


# print(my_function(103))
# print(my_function(101))
# print(my_function(102))
# print(my_function(100))
# print(my_function(111))
# print(my_function(113))
# print(my_function(112))
# print(my_function(105))


# def my_function(number):
#     while number != 0:
#         print(number % 10)
#         number = number // 10


# my_function(1234)


# print(ord('a'))
# print(ord('b'))

# TODO
"""
برنامه ای بنویسید که معادل عددی کاراکتر های کلمه زیر را نمایش دهد
python

سپس مجموع اعداد را محاسبه نمائید

"""
# total = 0
# for char in 'python':
#     total += ord(char)
#     print(ord(char))
# print("total is:", total)


"""
با حلقه وایل
"""


# name = 'python'
# i = 0
# total = 0
# while i < len(name):
#     total += ord(name[i])
#     print(ord(name[i]))
#     i += 1

# print("total is:", total)


# favorite_food = {}
# for i in range(4):
#     name = input("Enter a name: ")
#     food = input("Enter food name: ")
#     favorite_food[name] = food

# print("favorite foods:", favorite_food)


"""
Do it with while loop
"""
favorite_food = {}

i = 0
while i < 2:
    name = input("Enter a name: ")
    food = input("Enter a food name: ")
    price = float(input("Enter food's price: "))

    favorite_food[name] = [food, price]
    i += 1

print("favorite foods:", favorite_food)
