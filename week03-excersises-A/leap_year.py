
# Get the year from the user
year = int(input("Type the year: "))

# Define a flag, make an assumption that it's not a leap year
is_leap = False 

# If year is divisible by 4 
if year % 4 == 0:

    # If year is divisible by 100
    if year % 100 == 0:

        # If year is divisible by 400
        if year % 400 == 0:
            # LEAP
            is_leap = True 

        # Else
        else:
            # NOT LEAP
            is_leap = False
    # Else 
    else:
        # LEAP
        is_leap = True
# Else 
else:
    # NOT LEAP
    is_leap = False 
    

# Check the flag and give the answer if leap year

if is_leap:
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")