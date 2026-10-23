
day = int(input("Day (1-31 depending on month): "))
month = int(input("Month (1-12): "))
year = int(input("Year: "))

correct = True

# Check month first, because this defines the day
# February
if month == 2:
    is_leap = False 
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap = True 
            else:
                is_leap = False
        else:
            is_leap = True
    else:
        is_leap = False 

    if is_leap:
        if day < 1 or day > 29:
            correct = False
    else:
        if day < 1 or day > 28:
            correct = False

# Apr, Jun, Sep, Nov
elif month in [4, 6, 9, 11]:
    if day < 1 or day > 30:
        correct = False
# Any other month
else:
    if day < 1 or day > 31:
        correct = False

if correct:
    print(f"{day}/{month}/{year} is correct")
else:
    print(f"{day}/{month}/{year} is invalid")