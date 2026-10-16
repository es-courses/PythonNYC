
prices = [25, 4, 10, 6, 78, 12, 11, 3, 38]

print(len(prices))

# Print the last element of the list
print(prices[-1])

# Print the value in the middle 

pos = len(prices) // 2
print(pos)
print(prices[pos])

# Print a list using range
print("Print List using range")
for i in range(0, len(prices)):
    print(prices[i])

# Print using for-each
print("Print List using for-each")
for value in prices:
    print(value)

print(f"MAX: {max(prices)}")
print(f"MIN: {min(prices)}")
print(f"TOTAL: {sum(prices)}")

max_value = 0
for value in prices:
    if value > max_value:
        max_value = value
print(f"MAX using hard way: {max_value}")

print(prices[2:6])
print(prices[5:])
print(prices[:6])

s = "This is a string of characters"
print(s[0])
print(s[-1])
print(len(s))
print(s[3:7])