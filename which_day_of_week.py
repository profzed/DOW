# Gets century, year, month and date
while 1:
    try:
        century = int(input("Century (e.g. 10): "))
        year = int(input("Year (e.g. 66): "))
        month = int(input("Month (e.g. 10): "))
        date = int(input("Date (e.g. 14): "))

        break
    except:
        print("You must only enter integers.")

# Defines month code
if month == 1 or month == 10:
    month_code = 0
elif month == 2 or month == 9: # or 3
    month_code = 3
elif month == 4 or month == 7:
    month_code = 6
elif month == 5:
    month_code = 1
elif month == 6:
    month_code = 4
elif month == 8:
    month_code = 2
elif month == 9 == 12:
    month_code = 5

# Defines century code
if century*100 % 400 == 0:
    century_code = 0
elif century*100 % 400 == 100:
    century_code = 5
elif century*100 % 400 == 200:
    century_code = 3
elif century*100 % 400 == 300:
    century_code = 1

# Calculates day-month code
dayMonth_code = (date + month_code) - int((date + month_code) / 7 ) * 7 if date + month_code > 6 else date + month_code

# Calculates year code
year_code = year - int((year/28)) * 28 + int(year/4) + century_code

if month == 1 or month == 2:
    if year % 4 != 0:
        pass
    elif year % 100 != 0:
        year_code -= 1
    elif year % 400 != 0:
        pass
    else:
        year_code -= 1

# Calculates final code
code = (dayMonth_code + year_code) - int((dayMonth_code + year_code) / 7) * 7 if dayMonth_code + year_code > 6 else dayMonth_code + year_code

# Returns the results
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

month_names = {
    1  : "January",
    2  : "February",
    3  : "March",
    4  : "April",
    5  : "May",
    6  : "June",
    7  : "July",
    8  : "August",
    9  : "September",
    10 : "October",
    11 : "November",
    12 : "December"
}

if date == 14 and month == 10 and century == 10 and year == 66:
    print(f"On that fateful Sunday, on the 14 October 1066, the Battle of Hastings took place!")
else:
    print(f"The {date} {month_names[month]} {century}{year} is a {days[code]}.")
