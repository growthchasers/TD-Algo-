months_days = {
    "January": 31,
    "February": 28, 
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

date = input('entre la date sous forme(september 2024): ')
month, year = date.split(' ')
year = int(year)
if month == "February" and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    days = 29
else:
    days = months_days.get(month.capitalize())

if days:
    print(f"{month.capitalize()} {year} has {days} days.")
else:
    print('Invalid Month')