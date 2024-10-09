"""
This module provides a simple calculator that performs basic arithmetic operations.
It prompts the user for two numbers and an operation, then displays the result.

Functions:
- prompt(key): Prints a message based on the provided key.
- invalid_number(number_str): Checks if the provided string is a valid number.
"""

# Ask the user for the first number.
# Ask the user for the second number.
# # Ask the user for an operation to perform.
# Perform the operation on the two numbers.

import json

LANGUAGE = 'en'

with open('calculator_messages.json', 'r', encoding='utf-8') as file:
    MESSAGES = json.load(file)

def prompt(key):
     """
    Prints a message based on the provided key.

    Args:
        key (str): The key to look up the message in the MESSAGES dictionary.
    """
    message = messages(key, LANGUAGE)
    print(f"==> {message}")

def invalid_number(number_str):
     """
    Checks if the provided string is a valid number.

    Args:
        number_str (str): The string to check.

    Returns:
        bool: True if the string is not a valid number, False otherwise.
    """
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def messages(message, lang='en'):
    """
    Retrieves a message from the MESSAGES dictionary based on the provided key and language.

    Args:
        message (str): The key to look up the message.
        lang (str): The language code (default is 'en').

    Returns:
        str: The message corresponding to the provided key and language.
    """
    return MESSAGES[lang][message]

prompt('welcome')

while True:
    prompt("first_number")
    number1 = input()

    while invalid_number(number1):
        prompt("invalid_number")
        number1 = input()

    prompt("second_number")
    number2 = input()

    while invalid_number(number2):
        prompt("invalid_number")
        number2 = input()

    prompt("operation")

    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt("must_choose")
        operation = input()


    match operation:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            output = float(number1) // float(number2)

    print(f'The result is: {output}')


    prompt("another_calculation")
    answer = input()
    if answer and answer[0].lower() != 'y':
        break

while answer not in ["y", "n"]:
    prompt("invalid_choice")
    answer = input()
