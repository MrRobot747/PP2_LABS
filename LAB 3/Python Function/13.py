import random

def guess_number():
    name = input("Hello! What is your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = int(input("Take a guess.\n"))
        attempts += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break

# Запуск игры
guess_number()
