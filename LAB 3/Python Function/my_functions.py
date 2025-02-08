# my_functions.py

import math
import random

def has_33(nums):
    return any(nums[i] == nums[i+1] == 3 for i in range(len(nums)-1))

def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

def sphere_volume(r):
    return (4/3) * math.pi * r**3

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

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
