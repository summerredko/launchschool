# Isn't It Odd?
# def is_odd(num):
#     return abs(num) % 2 == 1
    
# print(is_odd(4))
# print(is_odd(5))
# print(is_odd(-5))

# Odd Numbers
# for n in range(1, 100, 2):
#     if n % 2 == 1:
#         print(n)

# Even Numbers
# for n in range(2, 100, 2):
#     if n % 2 == 0:
#         print(n)

# How big is the room?
# def room_in_meters(length, width):
#     meters = float(length) * float(width)
#     print(f'The room is: {meters} square meters')

# def room_in_feet(length, width):
#     feet = float(length) * float(width) * 10.7639
#     print(f'The room is: {feet} square feet')

# length = (float(input("Enter the length of the room in meters: ")))
# width = (float(input("Enter the width of the room in meters: ")))

# room_in_meters(length,  width)
# room_in_feet(length, width)


# system_of_measurement = int(input("Press 1 for metric or 2 for imperial: "))

# length = float(input("Enter the length of the room: "))
# width = float(input("Enter the width of the room: "))

# area_in_meters = length * width
# area_in_feet = area_in_meters * 10.7639

# if system_of_measurement == 1:
#     print(f"The area of the room is {area_in_meters:.2f} "
#       f"square meters ({area_in_feet:.2f} square feet)")

# if system_of_measurement == 2:
#     print(f"The room is {area_in_feet:.2f} "
#       f"square feet ({area_in_meters:.2f} square meters)")

# Tip Calculator
# What is the bill? 200
# What is the tip percentage? 20

# The tip is $40.00
# The total is $240.00

# bill_total = float(input("What is the bill total? "))
# tip_rate = float(input("What is the tip rate? "))

# tip_total = bill_total * (tip_rate / 100)
# final_balance = bill_total + tip_total

# print(f'The tip is: {tip_total:.2f}')
# print(f'The bill is: {final_balance:.2f}')

# Sum or Product of Consecutive Integers
# def compute_sum_or_product(n, choice):
#     if choice == "s":
#         return sum(range(1, n + 1))
#     elif choice == 'p':
#         product = 1
#         for i in range(1, n + 1):
#             product *= i
#         return product
#     else:
#         raise ValueError("Invalid choice. Enter 's' for sum or 'p' for product.")


# n = int(input("Enter a number greater than 0: "))
# choice = input('Enter "s" to compute the sum or "p" to compute the product: ' )

# final_number = compute_sum_or_product(n, choice)

# print(f'The product of the integers between 1 and {n} is {final_number}')

# Short Long Short
# def add_strings(str1, str2):
#     if len(str1) < len(str2):
#         return str1 + str2 + str1
#     else:             
#         return str2 + str1 + str2

# print(add_strings("aaaaaaaaaa", "bb"))

# Leap Years (Part 1)
# def is_leap_year(year):
#     year = abs(int(year))

#     if year <= 0:
#         return 'Invalid number'
    
#     return True if (
#         (year % 400 == 0) or
#         ((year % 4 == 0) and (year % 100 != 0))
#     ) else False

# # These examples should all print True
# print(is_leap_year(2) == False)
# print(is_leap_year(3) == False)
# print(is_leap_year(4) == True)
# print(is_leap_year(1000) == False)
# print(is_leap_year(1100) == False)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == False)
# print(is_leap_year(1751) == False)
# print(is_leap_year(1752) == True)
# print(is_leap_year(1753) == False)
# print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)

# Leap Year (Part 2)
# Julian calendar prior to 1752, and the Gregorian calendar starting in 1752
# def is_leap_year(year):
#     year = abs(int(year))

#     if year <= 0:
#         return 'Invalid number'
    
#     return True if (
#         (year < 1752 and year % 4 == 0) or
#         (year % 400 == 0) or
#         ((year % 4 == 0) and (year % 100 != 0))
#     ) else False

# # These examples should all print True
# print(is_leap_year(1) == False)
# print(is_leap_year(2) == False)
# print(is_leap_year(3) == False)
# print(is_leap_year(4) == True)
# print(is_leap_year(1000) == True)
# print(is_leap_year(1100) == True)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == True)
# print(is_leap_year(1751) == False)
# print(is_leap_year(1752) == True)
# print(is_leap_year(1753) == False)
# print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)

# Multiples of 3 and 5
# def multisum(n):
#     total = 0
#     for i in range(1, n + 1):
#         if i % 3 == 0 or i % 5 == 0:
#             total += i
#     return total

# # These examples should all print True
# print(multisum(3) == 3)
# print(multisum(5) == 8)
# print(multisum(10) == 33)
# print(multisum(1000) == 234168)

# UTF-16 String Value
# def utf16_value(string):
#     total = 0
#     for element in string:
#         values = ord(element)
#         total += values
#     return total

# # These examples should all print True
# print(utf16_value('Four score') == 984)
# print(utf16_value('Launch School') == 1251)
# print(utf16_value('a') == 97)
# print(utf16_value('') == 0)

# # The next three lines demonstrate that the code
# # works with non-ASCII characters from the UTF-16
# # character set.
# OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
# print(utf16_value(OMEGA) == 937)
# print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)

# Welcome Stranger
# def greeting(name, job):
#     return f'Hello {" ".join(name)}! Nice to have a {job['title']} {job['occupation']} around.'

# greeting = greetings(
#     ["John", "Q", "Doe"],
#     {"title": "Master", "occupation": "Plumber"},
# # )
# print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.


# Greeting a User
# name = ['John', 'Doe']
# job = {
#     'title' : 'Master',
#     'occupation' : 'Plumber',
# }

# print(greeting(name, job))

# Greeting a User
# name = input('What is your name? ')

# Multiplying Two Numbers

# def multiply(n1, n2):
#     return n1 * n2

# print(multiply(5, 3) == 15)  # True

# Squaring an Argument

# def multiply(num1, num2):
#     return num1 * num2

# def square(number):
#     return multiply(number, number)

# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True

# Floating Point Arithematic
# def prompt(message):
#     print(f"==> {message}")

# def addition(num1, num2):
#     return num1 + num2

# def subtraction(num1, num2):
#     return num1 - num2

# def product(num1, num2):
#     return num1 * num2

# def quotient(num1, num2):
#     return num1 / num2

# def floor_quotient(num1, num2):
#     return num1 // num2

# def remainder(num1, num2):
#     return num1 % num2

# def power(num1, num2):
#     return num1 ** num2

# prompt('Welcome to Floating Point Arithematic')

# prompt("Enter your first number: ")
# num1 = float(input())
# prompt("Enter your second number: ")
# num2 = float(input())


# prompt(f'{num1} + {num2} = {addition(num1, num2)}')
# prompt(f'{num1} - {num2} = {subtraction(num1, num2)}')
# prompt(f'{num1} * {num2} = {product(num1, num2)}')
# prompt(f'{num1} / {num2} = {quotient(num1, num2)}')
# prompt(f'{num1} // {num2} = {floor_quotient(num1, num2)}')
# prompt(f'{num1} % {num2} = {remainder(num1, num2)}')
# prompt(f'{num1} ** {num2} = {power(num1, num2)}')

# def calculate(first, second, operation):
#     match operator:
#         case '+': return first + second
#         case '-': return first - second
#         case '*': return first * second
#         case '/': return first / second
#         case '//': return first // second
#         case '%': return first % second
#         case '**': return first ** second

# first = float(input("==> Enter your first number:  "))
# second = float(input("==> Enter your second number: "))

# for operator in ['+', '-', '*', '/', '//', '%', '**']:
#     operation = f'{first} {operator} {second}'
#     result = calculate(first, second, operator) 
#     print(f'==> {operation} = {result}')

# The End Is Near But Not Here
# def penultimate(string):
#     return string.split(" ")[-2]

# # These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

# Exlcusive Or

# def xor(a, b):
#     if (a and not b) or (b and not a):
#         return True
    
#     return False

# def xor(a, b):
# return bool((a and not b) or (b and not a))

# print(xor(5, 0) == True)
# print(xor(False, True) == True)
# print(xor(1, 1) == False)
# print(xor(True, True) == False)

# Odd Lists

# function that returns a list
# contains every other element of a list
# passed in as an argument
# 1st, 3rd, 5th, and so on elements of the argument list

# def oddities(lst):

    #slicing
    # return lst[::2]

    #for loop
    # odd_index = []
    # for i in range(len(lst)):
    #     if i % 2 == 0:
    #         odd_index.append(lst[i])
    # return odd_index

    #list comprehension
#     return [element for element in lst
#                 if lst.index(element) % 2 == 0 ]

# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
# print(oddities([1, 2, 3, 4]) == [1, 3])        # True
# print(oddities(["abc", "def"]) == ['abc'])     # True
# print(oddities([123]) == [123])                # True
# print(oddities([]) == [])                      # True

# How Old is Teddy?

# randomly generate and print Teddy's age
# 20 and 100, inclusive
# import random

# age = random.randint(20, 100)
# print(f'Teddy is {age} years old!')

# When Will I Retire?
# displays when the user will retire
# how many years she has to work till retirement

# asks for age
# calculate age to 65
# print 
# What is your age? 30
# At what age would you like to retire? 70

# It's 2024. You will retire in 2064.
# You have only 40 years of work to go!
# import datetime

# current_age = int(input("What is your age? "))
# retire_age = int(input("What age would you like to retire? "))

# current_year = datetime.datetime.now().year

# years_to_go = retire_age - current_age
# number_of_years = current_year + years_to_go


# print(f"""
# It's {current_year}. You will retire in {number_of_years}. 
# You only have {years_to_go} more years of work to go!
# """)

# Get Middle Character
# function that takes a non-empty string argument
# returns the middle character(s) of the string
# If the string has an odd length, you should return exactly one character
# If the string has an even length, you should return exactly two characters

# def center_of(string):
#     if len(string) % 2 == 1: #odd
#         middle_index = len(string) // 2
#         return string[middle_index]
#     else:
#         left_index = len(string) // 2 - 1
#         return string[left_index:left_index + 2]



# print(center_of('I Love Python!!!') == "Py")    # True (odd)
# print(center_of('Launch School') == " ")        # True (even)
# print(center_of('Launchschool') == "hs")        # True
# print(center_of('Launch') == "un")              # True
# print(center_of('Launch School is #1') == "h")  # True
# print(center_of('x') == "x")                    # True

# Always Return Negative
# function that takes a number as an argument
# If the argument is a positive number, return the negative of that number
# If the argument is a negative number, return it as-is

# def negative(number):
#     return -abs(number)

# print(negative(5) == -5)      # True
# print(negative(-3) == -3)     # True
# print(negative(0) == 0)       # True

# Repeat Yourself
# function that takes two arguments, a string and a positive integer
# then prints the string as many times as the integer indicates

def repeat(string, number):

    if number <= 0:
        print('Invalid. Number must be greater than 0.')

    # while loop
    # counter = 0
    # while counter < number:
    #     print(string)
    #     counter += 1

    # for loop
    # if number <= 0:
    #     print('Invalid. Number must be greater than 0.')
    # else:
    #     for i in range(number):
    #         print(string)

# repeat("hell yeah", 3)
# repeat("f-no", -3)
    

# ddaaiillyy ddoouubbllee
# Function that takes a string argument
# returns a new string that contains the value of the original string
# with all consecutive duplicate characters collapsed into a single character


# def crunch(string):
#     last_seen = None
#     result = []

#     for char in string:
#         if char != last_seen:
#             result.append(char)
#         last_seen = char

#     final = ''.join(result)

#     return final


# # These examples should all print True
# print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('ggggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')

# Bannerizer
# Function that takes a short line of text and prints it within a box


# def print_box(text, width):
#     # text = text.splitlines()
#     # maxlen = max(len(s) for s in text)
#     # colwidth = maxlen + 2

#     # print('+' + '-'*colwidth + '+')
#     # for s in text:
#     #     print('| %-*.*s |' % (maxlen, maxlen, s))
#     #     print('+' + '-'*colwidth + '+')

#     horizontal = f'+{"-" * (width + 2)}+'
#     line = f'| {" " * width} |'

#     if len(text) > width:
#         text = text[:width]


#     print(horizontal)
#     print(line)
#     print(f'| {text:<{width}} |')
#     print(line)
#     print(horizontal)

# print_box("Fuck you, America!", 20)

# Strings Strings
# Function that takes one argument, a positive integer
# returns a string of alternating '1's and '0's, always starting with a '1'
# The length of the string should match the given integer

# def stringy(number):

    # for i in range(number):
    #     if number % 2 == 0:
    #         return "10" * (number // 2)
    #     else:
    #         return "10" * (number // 2) + "1"

    # result = ""
    # for i in range(number):
    #     digits = "1" if i % 2 == 0 else "0"
    #     result += digits
    
    # return result

# def stringy(num):
#     string = ''
#     for i in range(num):
#         string += str((i + 1) % 2)
#     return string


# print(stringy(6) == "101010")           # True
# print(stringy(9) == "101010101")        # True
# print(stringy(4) == "1010")             # True
# print(stringy(7) == "1010101")          # True

# Right Triangles
# Function that takes a positive integer as an argument
# and prints a right triangle whose sides each have n stars. 
# the diagonal side should have one end at the lower-left of the triangle
# and the other end at the upper-right.

# def triangle(number):
#     for i in range(number):
#         tree = "*" * i
#         print(f"{tree : >{number}}")

# def triangle(height):
#     for num in range(1, height + 1):
#         spaces = height - num
#         stars = num
#         print(f'{" " * spaces}{"*" * stars}')
        

# triangle(10)

# Return values for and or operators
# print('a' and 2 < 3) # 'a' and True => True
# print('' or ('a', 'b')) # []
# print('a' or 2 < 3) # 'a'
# print('a' and {}) 
# print(0 and 2 < 3 or 'c' > 'a')

# Pop and truthiness
# lst1 = [0, 1, 2, 3]
# lst2 = lst1.pop(0) or lst1.pop()

# if lst2:
#     print(lst2)
# else:
#     print(2, lst1)

# Madlibs
# Prompts for a noun, a verb, an adverb, and an adjective
# injects them into a story that you create.

# def prompt(message):
#     print(f'==> {message}')

# def madlib():
#     prompt(title)
#     print(story)

# noun = input("Enter a noun: ")

# noun2 = input("Enter another noun: ")

# verb = input("Enter a verb: ")

# adjective = input("Enter an adjective: ")

# adjective2 = input("Enter another adjective: ")


# title = f'Title: The Adventure of the {noun}'

# story = f"""
# One day, a {noun} decided it was time to {verb}. 
# It packed its favorite {noun2} and set off on an adventure.
# Along the way, it saw a lot of {adjective} sights and met some {adjective2} friends. 
# By the end of the day, the {noun} was tired but very happy. 
# It had finally gone on the {adjective} adventure it had always dreamed of!
# """

# madlib()


# Double Doubles
# Function that returns the number provided as an argument 
# multiplied by two
# If the argument is a double number, return the double number as-is.

# def twice(number):
#     # string = str(number)

#     # if string[:len(string)//2] == string[len(string)//2:]:
#     #     return number

#     # return int(string) * 2



#     string = str(number)
#     half = len(string) // 2

#     return number * 2 if string[:half] != string[half:] else number


# print(twice(37) == 74)                  # True
# print(twice(44) == 44)                  # True
# print(twice(334433) == 668866)          # True
# print(twice(444) == 888)                # True
# print(twice(107) == 214)                # True
# print(twice(103103) == 103103)          # True
# print(twice(3333) == 3333)              # True
# print(twice(7676) == 7676)              # True


# Grade Book
# Function that determines the mean (average) of the three scores passed to it
# returns the letter associated with that grade.

#Numerical score letter grade list:

# 90 <= score <= 100: 'A'
# 80 <= score < 90: 'B'
# 70 <= score < 80: 'C'
# 60 <= score < 70: 'D'
# 0 <= score < 60: 'F'

# def get_grade(n1, n2, n3):
#     mean = (n1 + n2 + n3) / 3

#     match mean:
#         case _ if mean >= 90:
#             return "A"
#         case _ if mean >= 80 and mean < 90:
#             return "B"
#         case _ if mean >= 70 and mean < 80:
#             return "C"
#         case _ if mean >= 60 and mean < 70:
#             return "D"
#         case _ if mean >= 0 and mean < 60:
#             return "F"


# print(get_grade(95, 90, 93) == "A")      # True
# print(get_grade(50, 50, 95) == "D")      # True

# Clean up the words
# Function that returns a string with all of the non-alphabetic characters replaced by spaces
# If one or more non-alphabetic characters occur in a row, 
# you should only have one space in the result

# def clean_up(text):
#     # if string.isalpha():
#     #     return string
    
#     # new_string = ""
#     # for char in string:
#     #     if not char.isalpha():
#     #         new_string += " "
#     #     else:
#     #         new_string += char

#     # result = ""
#     # prev_char = None
#     # for char in new_string:
#     #     if char != prev_char:
#     #         result += char
#     #         prev_char = char
#     # return result

#     clean_text = ''

#     for idx, char in enumerate(text):
#         if char.isalpha():
#             clean_text += char
#         elif idx == 0 or clean_text[-1] != ' ':
#             clean_text += ' '

#     return clean_text
            

# print(clean_up("---what's my +*& line?") == " what s my line ")

# What Century is That?
# Function that takes a year as input and returns the century
# The return value should be a string that begins with the century number
# and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number
# New centuries begin in years that end with 01

# If it is a four digit year (such as 2023), 
# we add 1 to the first two digits (20+1= 21st century)

# def century(year):
    # century = (year + 99) // 100

    # if 11 <= century % 100 <= 13:
    #     suffix = "th"
    # elif century % 10 == 1:
    #     suffix = "st"
    # elif century % 10 == 2:
    #     suffix = "nd"
    # elif century % 10 == 3:
    #     suffix = "rd"
    # else:
    #     suffix = "th"
    
    # return f'{century}{suffix}'

# def century(year):
#     century_number = year // 100 + 1

#     if year % 100 == 0:
#         century_number -= 1

#     suffix = century_suffix(century_number)
#     return f'{century_number}{suffix}'

# def century_suffix(century_number):
#     last_two = century_number % 100
#     last_digit = century_number % 10

#     match last_two:
#         case 11 | 12 | 13:
#             return 'th'

#     match last_digit:
#         case 1:
#             return 'st'
#         case 2:
#             return 'nd'
#         case 3:
#             return 'rd'
#         case _:
#             return 'th'


# print(century(2000) == "20th")          # True
# print(century(2001) == "21st")          # True
# print(century(1965) == "20th")          # True
# print(century(256) == "3rd")            # True
# print(century(5) == "1st")              # True
# print(century(10103) == "102nd")        # True
# print(century(1052) == "11th")          # True
# print(century(1127) == "12th")          # True
# print(century(11201) == "113th")        # True
