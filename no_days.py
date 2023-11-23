def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# TODO: Add more code here 👇


def days_in_month(yr, mn):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap = is_leap(yr)
    if leap and mn == 2:
        return 29
    else:
        return month_days[mn - 1]


# 🚨  Do NOT change any of the code below
y = int(input())  # Enter a year
m = int(input())  # Enter a month
d = days_in_month(y, m)
print(d)
