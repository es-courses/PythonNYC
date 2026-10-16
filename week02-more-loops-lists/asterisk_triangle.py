
# Get a number n from the user
n = int(input("Give a number: "))

# Repeat n times, from 1 to n included (i)
for i in range(1, n+1):
    
    # Repeat i times
    for j in range(i):
        
        # print 1 asterisk - stay in the same line
        print('*', end=' ')

    # Go to the next line
    print()


print("Using While")
i = 1
while i <= 5:
    for j in range(i):
        print('*', end=' ')
    print()
    i = i + 1