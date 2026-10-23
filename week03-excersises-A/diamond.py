
# Prints a diamond, e.g. if n is 5
#       * 
#     * * *
#   * * * * *
#     * * *
#       * 


n = int(input("Gine n: "))

# Print the upper part
repetitions = n // 2 +1
spaces = n // 2
asterisks = 1 

for i in range(repetitions):
    for s in range(spaces):
        print(' ', end=' ')
    for a in range(asterisks):
        print('*', end=' ')
    print()
    spaces = spaces - 1
    asterisks = asterisks + 2

# Print the lower part
repetitions = n // 2
spaces = 1
asterisks = n - 2

for i in range(repetitions):
    for s in range(spaces):
        print(' ', end=' ')
    for a in range(asterisks):
        print('*', end=' ')
    print()
    spaces = spaces + 1
    asterisks = asterisks - 2