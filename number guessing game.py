import random

number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if guess > number:
        print("Too High")

    elif guess < number:
        print("Too Low")

    else:
        print("Correct Guess!")
        print("Attempts =", attempts)
        break