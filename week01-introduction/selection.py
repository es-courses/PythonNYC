
age = int(input("Your Age: "))

if age < 18:
    print("Young, your fees are 200")
elif age < 50:
    print("Middle age, fees are 350")
else:
    print("Old, fees are 450")

print("Please pay by the end of month")