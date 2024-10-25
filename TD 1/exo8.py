# exo 8
print('----------exo8 started---------')

day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

days_in_month = [31, 29 if is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month < 1 or month > 12:
    print("Invalid month.")
elif day < 1 or day > days_in_month[month - 1]:
    print("Invalid day.")
else:
    print("The date is valid.")


print('----------exo8 finished---------')