"""
2016 => leap
2020 => leap
2024 => leap

2100 => not leap
2200 => not leap
2300 => not leap

2000 => leap
2400 => leap


"""


def is_leap_year(year):
    if year % 400 == 0:
        return f"{year} is leap year"
    elif year % 100 == 0:
        return f"{year} is not leap year"
    elif year % 4 == 0:
        return f"{year} is leap year"
    else:
        return f"{year} is not leap year"
    
# print(is_leap_year(2016))
# print(is_leap_year(2020))
# print(is_leap_year(2024))
# print(is_leap_year(2100))
# print(is_leap_year(2200))
# print(is_leap_year(2300))
# print(is_leap_year(2000))
# print(is_leap_year(2400))


# is_valid_date(2005, 3, 29) => True
# is_valid_date(2005, 13, 32) => False

"""
month is 2 => maximum of days is 28  in leap year 29
otherwise 31
months => 1-12
days => 
if month is 9,4,6,11 => maximum 30
if 


"""