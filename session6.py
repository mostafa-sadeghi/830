# a = 4
# b = 4
#
# if a > b:
#     print("a is greater than b.")
# elif a < b:
#     print("a is less than b.")
# else:
#     print("a and b are equal.")


# number1 = 4
# number2 = 6
#
# if number1 >= number2:
#     print("number1 is greater than or equal to number2")
#
# elif number1 <= number2:
#     print("number1 is less than or equal to number2.")


# x = 3
# y = 3
# #
# if x == y:
#     print("x and y are equal")
#     print("blallalalal")
#
# if x != y:
#     print("x and y are not equal")


"""
برنامه ای بنویسید که دو عدد از ورودی دریافت نماید
و با هم مقایسه کند

اگر دوعدد برابر بودند
پیغام مناسبی را نمایش دهد


"""

# number1 = int(input("enter a number: "))
# number2 = int(input("enter a number: "))
# if number1 > number2:
#     print("number1 is greater")
# elif number2 > number1:
#     print("number2 is greater")
# else:
#     print("number1 = number2")

# TODO
"""
برنامه ای بنویسید که نمره یک دانش آموز را از ووردی دریافت نماید و اگر نمره وی از 90 بالاتر بود
A 
را پرینت نماید
اگر نمره او از 80 بالاتر باشد
B
 را پرینت نماید
 
 اگر نمره او از 70 بالاتر باشد
 C 
 را پرینت نماید
 در غیر اینصورت
 F
  را پرینت نماید
"""

a = 2
b = 3
c = 4

if a < b and a < c:
    print("a is the smallest")

name = input("enter your name: ")
if name == "sara" or name == "artin":
    print(f"welcome, {name} is valid.")
else:
    print(f"{name} is not valid.")
