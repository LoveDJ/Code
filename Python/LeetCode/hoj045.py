year = int(input().strip().lstrip('0'))
month = int(input().strip().lstrip('0'))
day = int(input().strip().lstrip('0'))

day_arr01 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_arr02 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

is_leap_year = False
if year%4 == 0 and year%100 != 0: is_leap_year = True
if year%400 == 0: is_leap_year: is_leap_year = True

days = 0
for i in range(month-1):
    if is_leap_year: days += day_arr02[i]
    else: days += day_arr01[i]
days += day
print(days)



