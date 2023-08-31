# def is_odd_or_even(number):
#     if number % 2 == 0:
#         return "even"
#     else:
#         return "odd"
    

# print(is_odd_or_even(2))
# print(is_odd_or_even(3))
# print(is_odd_or_even(312))
# print(is_odd_or_even(313))
# num = int(input("Enter a number: "))
# print(is_odd_or_even(num))

# def area(w, h):
#     return w * h

# print(area(2,4))
# width = int(input("Enter the width: "))
# height = int(input("Enter the height: "))
# print(area(width, height))



# def permiter(w, h):
#     return 2 * (w + h)
# print(permiter(2,4))

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"
    if number % 3 == 0:
        return "fizz"
    if number % 5 == 0:
        return "buzz"
    return number

print(fizzbuzz(15))
print(fizzbuzz(3))
print(fizzbuzz(34))
print(fizzbuzz(36))
print(fizzbuzz(130))