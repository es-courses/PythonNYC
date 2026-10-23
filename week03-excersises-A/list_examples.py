
data = [12, 15, 90, 28, 4, 16, 27, 29, 54, 10, 3, 41, 64]

# Find the minimum - without using python's min function
min_value = data[0]

for i in range(1, len(data)):
    if data[i] < min_value:
        min_value = data[i]

print(f"MIN: {min_value}")

min_value = data[0]

for value in data[1:]:
    if value < min_value:
        min_value = value

print(f"MIN: {min_value}")

max_value = data[0]

for value in data[1:]:
    if value > max_value:
        max_value = value

print(f"MAX: {max_value}")

# Find Average
total = data[0]

for value in data[1:]:
    total = total + value 

average = total / len(data)

print(f"AVG: {average}")


    