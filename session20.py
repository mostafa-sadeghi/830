# def my_function_1(row, column):
#     if row % 2 == column % 2:
#         return 'white'
#     else:
#         return "black"
    
# print(my_function_1(1,1))
# print(my_function_1(1,3))
# print(my_function_1(2,2))
# print(my_function_1(2,3))


# 1h -> 3600s
# 1m -> 60s
# 125 -> 2m 5s
# 3610 -> 1h 10s

# def my_function_2(time):
#     if time >= 3600:
#         h = time // 3600
#         time = time % 3600
#     else:
#         h = 0

#     if time >= 60:
#         m = time // 60
#         time = time % 60

#     else:
#         m = 0
#     s = time
#     return (h, m, s)

# print(my_function_2(50))
# print(my_function_2(55))
# print(my_function_2(60))
# print(my_function_2(65))
# print(my_function_2(3650))
# print(my_function_2(3610))
# print(my_function_2(3600))



numbers = [28, 25, 42, 2, 28]
def my_function_3(numbers):
    smallest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n

    return smallest

print("smallest is :",my_function_3(numbers))

