"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Eva Vallušová
email: eva.vallusova@gmail.com
discord: energetic_avocado_65638
"""

import random
import time

section_splitter = "-" * 40


def unique_four_digit_generation() -> int:
    all_digits = list("0123456789")

    first_digit = random.choice(all_digits[1:])
    all_digits.remove(first_digit)

    another_digits = random.sample(all_digits, 3)

    return int(first_digit + "".join(another_digits))


def is_input_valid(user_try: str) -> bool:
    if len(user_try) != 4:
        print("Please select exactly 4 digits.")
        return False
    elif user_try[0] == "0":
        print("Your try cannot start with 0.")
        return False
    elif not user_try.isdigit():
        print("Please select digits only (0-9).")
        return False
    elif len(set(user_try)) != 4:
        print("Digits must be unique.")
        return False
    else:
        return True


def count_bulls_cows(user_input: str, secret_number: int) -> tuple[int, int]:
    list_user_input = list(user_input)
    list_secret_number = list(str(secret_number))

    count_bulls = 0
    count_cows = 0

    for i in range(len(list_secret_number)):
        if list_user_input[i] == list_secret_number[i]:
            count_bulls += 1
        elif list_user_input[i] in list_secret_number:
            count_cows += 1
    return count_bulls, count_cows


def introduction_text():
    print("Hi there!")
    print(section_splitter)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(section_splitter)


def get_performance_feedback(attempts: int) -> str:
    if attempts <= 4:
        return "Excellent!"
    elif attempts <= 10:
        return "Good job!"
    elif attempts <= 16:
        return "Not bad!"
    else:
        return "Keep practicing!"


introduction_text()

random_four_digits = unique_four_digit_generation()
start_time = time.time()
attempts = 0

# print(random_four_digits)  # Uncomment for testing


while True:
    user_try = input("Enter a number:")
    attempts += 1

    if not is_input_valid(user_try):
        continue

    count_bulls, count_cows = count_bulls_cows(user_try, random_four_digits)

    bull_word = "bull" if count_bulls == 1 else "bulls"
    cow_word = "cow" if count_cows == 1 else "cows"

    print(f"{count_bulls} {bull_word}, {count_cows} {cow_word}")

    if count_bulls == 4:
        end_time = time.time()
        duration = round(end_time - start_time, 2)

        print(f"Correct, you've guessed the right number in {attempts} attempts!")
        print(section_splitter)
        print(f"Time taken: {duration} seconds.")
        print(section_splitter)
        print(get_performance_feedback(attempts))
        break
