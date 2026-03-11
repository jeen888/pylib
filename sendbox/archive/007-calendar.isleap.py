def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

print(is_leap_year(2020))  # True
print(is_leap_year(2021))  # False


print("-" * 30)

# calendar 모듈을 이용한 윤년 계산
import calendar

print(calendar.isleap(2020))  # True
print(calendar.isleap(2021))  # False