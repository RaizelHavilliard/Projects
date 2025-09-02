"""
Module: Number to Words Converter

This module provides a function to convert integer numbers into their
English word representation. It handles numbers from 0 up to 999,999,999,999.

Dependencies:
- constants.py: should define three dictionaries/lists:
    - UNDER_20: mapping of numbers 0–19 to words
    - TENS: mapping of tens (20,30,...,90) to words
    - ABOVE_100: mapping of larger powers (100, 1000, 1_000_000, etc.) to words
"""

from constants import ABOVE_100, TENS, UNDER_20

def num_to_word(num):
    """
    Convert a number into its English word representation.

    Parameters:
    - num (int): The number to convert. Should be in the range 0–999,999,999,999.

    Returns:
    - str: The number in words.

    Algorithm:
    1. If the number is less than 20, return the corresponding word from UNDER_20.
    2. If the number is less than 100:
        a. If it is divisible by 10, return the corresponding word from TENS.
        b. Otherwise, return the tens word + the word for the remainder (units).
    3. If the number is 100 or higher:
        a. Find the largest key in ABOVE_100 that is <= num (pivot).
        b. Recursively convert the quotient (num // pivot) to words.
        c. Append the word corresponding to pivot.
        d. If there's a remainder, recursively convert it and append.
    """
    if num < 20:
        return UNDER_20[num]
    elif num < 100:
        remainder = num % 10
        if remainder == 0:
            return TENS[num // 10]
        return TENS[num // 10] + " " + UNDER_20[remainder]

    pivot = max([key for key in ABOVE_100 if key <= num])
    p1 = num_to_word(num // pivot)
    p2 = ABOVE_100[pivot]
    if num % pivot == 0:
        return f'{p1} {p2}'
    else:
        return f'{p1} {p2} {num_to_word(num % pivot)}'      


if __name__ == "__main__":
    """
    Command-line interface for number-to-word conversion.

    Steps:
    1. Prompt the user to enter an integer number.
    2. Check if the number is within the acceptable range (0 to 999,999,999,999).
    3. Print the number in words using num_to_word function.
    4. If the number is out of range, print an error message.
    """
    num = int(input("Enter a Number: "))
    if num >= 0 and num <= 999_999_999_999:
        print(num_to_word(num))
    else:
        print("Number out of range")
