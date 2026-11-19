
b = input("Give binary number: ")

exponent = len(b) - 1
num = 0

for ch in b:
    if ch == '1':
        num = num + (2**exponent)
    exponent -= 1

print(num)