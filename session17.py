# total = 0
# for i in range(10):
#     n = int(input("Enter a number: "))
#     if n % 2 != 0:
#         total += n

# print(f"sum of odd numbers : {total}")


numbers = []
for i in range(3):
    n = int(input("Enter a number: "))
    numbers.append(n)


print(numbers)

count = 0
new_number = int(input("Enter a number: "))
for num in numbers:
    if num == new_number:
        count += 1

print(f"{new_number} repeated {count} times")

