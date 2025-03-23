"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Eva Vallušová
email: eva.vallusova@gmail.com
discord: energetic_avocado_65638
"""

import random
import time


def unique_four_digit_generation() -> int:
    all_digits = list("0123456789")

    first_digit = random.choice(all_digits[1:])
    all_digits.remove(first_digit)

    another_digits = random.sample(all_digits, 3)

    return int(first_digit + "".join(another_digits))


def get_performance_feedback(attempts: int) -> str:
    if attempts <= 4:
        return "Excellent!"
    elif attempts <= 10:
        return "Good job!"
    elif attempts <= 16:
        return "Not bad!"
    else:
        return "Keep practicing!"


# Random number generation
random_four_digits = unique_four_digit_generation()

# TODO: delete at the end, showing secret number
print(random_four_digits)

section_splitter = "-" * 40

# Introductory text
print("Hi there!")
print(section_splitter)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(section_splitter)

start_time = time.time()
attempts = 0

while True:
    user_try = input("Enter a number:")
    attempts += 1

    # Validation
    if len(user_try) != 4:
        print("Please select exactly 4 digits.")
        continue
    elif user_try[0] == "0":
        print("Your try cannot start with 0.")
        continue
    elif not user_try.isdigit():
        print("Please select digits only (0-9).")
        continue
    elif len(set(user_try)) != 4:
        print("Digits must be unique.")
        continue

    # Input is valid
    user_input = int(user_try)
    list_user_input = list(str(user_input))
    list_secret = list(str(random_four_digits))

    count_bulls = 0
    count_cows = 0

    for i in range(len(list_secret)):
        if list_user_input[i] == list_secret[i]:
            count_bulls += 1
        elif list_user_input[i] in list_secret:
            count_cows += 1

    bull_word = "bull" if count_bulls == 1 else "bulls"
    cow_word = "cow" if count_cows == 1 else "cows"

    print(f"{count_bulls} {bull_word}, {count_cows} {cow_word}")

    if count_bulls == 4:
        end_time = time.time()
        duration = round(end_time - start_time, 2)

        print(f"Correct, you've guessed the right number in {attempts} attempts!")
        print(section_splitter)
        print(f"Time taken {duration}.")
        print(section_splitter)
        print(get_performance_feedback(attempts))
        break
