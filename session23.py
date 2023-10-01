"""
months => 1-12
days => 
if month is 9,4,6,11 => maximum 30
if month is 2 => maximum of days is 28  in leap year 29
otherwise 31
"""
# def is_leap_year(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
# def is_valid_date(year, month, day):

#     if is_leap_year(year) and month == 2 and day == 29:
#         return f"{month}-{day}-{year} is a valid Date"
#     if month in (1,3,5,7,8,10,12) and not (1<=day<=31):
#         return f"{month}-{day}-{year} is not a valid Date"
#     elif month in (4,6,9,11) and not (1<= day <=30):
#         return f"{month}-{day}-{year} is not a valid Date"
#     elif month == 2 and not(1<=day<=28):
#         return f"{month}-{day}-{year} is not a valid Date"
#     else:
#         return f"{month}-{day}-{year} is a valid Date"

# print(is_valid_date(2016,2,29))
# print(is_valid_date(2015,2,29))
# print(is_valid_date(2017,4,31))
# print(is_valid_date(2015,5,32))
# print(is_valid_date(2015,2,20))
# print(is_valid_date(2013,7,12))


import random
options = ('r', 'p', 's')
user_choice = input("Enter your choice(r, p, s): ")
system_choice = random.choice(options)


def rps_winner(user_choice, system_choice):
    if user_choice == 'r' and system_choice == 'p':
        return "system is the winner"
    elif user_choice == "r" and system_choice == "s":
        return "user is the winner"

    # TODO


print(rps_winner(user_choice, system_choice))
