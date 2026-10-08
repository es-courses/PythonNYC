import random 

# Generate a secret ramdom value 1-100
secret = random.randint(1, 100)
print(secret)

# Set a counter and a guess variable
counter = 0
guess = 0

# loop while guess is not equal to secret 
while guess != secret:

    # ask user to guess
    guess = int(input("Guess: "))

    # increase the counter 
    # counter = counter + 1
    counter += 1

    # if guess is greater than secret print DOWN
    if guess > secret:
        print("DOWN")
    # else if guess less than secter print UP
    elif guess < secret:
        print("UP")
    # else print found
    else:
        print(f"Found in {counter} guesses")

print("GAME OVER")
