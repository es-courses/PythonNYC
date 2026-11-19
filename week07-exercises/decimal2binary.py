
n = int(input("Give number: "))
binary = ''

temp = n
while temp > 0:
    r = temp % 2
    temp = temp // 2
    binary = str(r) + binary 

print(binary)
print(bin(n))