# string = "Aloha World!"
# string = string.lower()

# print(string)


# string = "Aloha World!"
# right = string.rjust(20)

# print(right)

# string = "Aloha World!"
# rev = string[::-1]

# print(rev)

# lst = ['fish', 'and', 'chips']

# print(lst[1])

# fruits = ["apple", "banana", "cherry", "peach", "watermelon"]

# print(fruits.index("cherry"))

# lst = ['fish', 'and', 'chips']

# print(lst[10])

# large_int = 10_123_123_123
# print(large_int)

# print(type(23.5))
# print(type('Call me Ishmael.'))
# print(type(False))
# print(type(0))
# print(type(None))

# name = "Victor"
# profession = "programmer"

# print("Hello {}. You are a {}.".format(name, profession))
# print(f'Hello {name}. You are a {profession}.')

# ice_cream_density = 10

# while ice_cream_density > 0:
#     print('Drip...')
#     ice_cream_density -= 1

# print('The ice cream melted.')


# from datetime import datetime

# friday = datetime.now()

# print(friday)


# from datetime import date

# today = date.today()

# today_year = today.year
# iso_year = today.isocalendar()[0]

# words = ["Hello", "World", "from", "Python"]

# new = " ".join(words)
# print(new)

# words ="Hello world, abc"
# if "xyz" in words:
#     print("Yep")
# else:
#     print("nope")

# for num in range(0, 11, 2):
#     print(num)

# for i in range(10, 0, -1):
#     print(i)

# print("Launch!")

# greeting = 'Aloha!'

# counter = 0
# while counter < 3:
#     print(greeting)
#     counter += 1

# for _ in range(3):
#     print(greeting)

# Write a for loop that iterates over the integers from 1 to 100
# prints the result of multiplying each integer by 2

# for num in range(1, 101):
#     print(num * 2)


# Write a while loop that prints the elements of lst at each index
# terminates after printing the last element of the list

# lst = []
# index = 0

# while index < len(lst):
#     print(lst[index])
#     index += 1

# friends = ['Sarah', 'John', 'Hannah', 'Dave']

# for friend in friends:
#     print(f'Hi, {friend}')

# for loop that iterates over the elements of the list cities
# prints the length of each string
# If the element is None, use the continue statement to skip forward

# cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
#           'Vienna', None, 'London', 'Beijing', None]


# for element in cities:
#     if element == None:
#         continue

#     print(len(element))

# while True:
#     print("and on")
#     break

# fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

# for fish in fish_list:
#     print(fish)
#     if fish == "Nemo":
#         break

# index = 0
# while index < len(fish_list):
#     print(fish_list[index])
#     if fish_list[index] == "Nemo":
#         break
#     index += 1

    
# while True:
#     print('Should I stop looping?')
#     answer = input()
#     if answer == "yes":
#         break

# Falsy: 0, [], {}, (), None, False, "", range(0), set()

# If statement that prints Yes! if random_number is 1, and No. if random_number is 0.

# import random
# # random_number = random.randint(0, 1)

# # if random_number == 1:
# #     print('Yes')
# # else:
# #     print('No')

# # print('Yes' if random_number == 1 else 'No')

# weather = ["sunny", "rainy", "snowy"]

# today_weather = random.choice(weather)

# # if today_weather == "sunny":
# #     print("Today's weather is sunny. It's as beautiful day!")
# # elif today_weather == "rainy":
# #     print("Today's weather is rainy. Grab your umbrella!")
# # elif today_weather == "snowy":
# #     print("Today's weather is snowy. Stay inside!")

# match today_weather:
#     case "sunny":
#         print("It's sunny!")
#     case "rainy":
#         print("It's rainy!")
#     case "snowy":
#         print("It's snowy!")

# def multiply(n1, n2):
#     return n1 * n2

# print(multiply(12, 4))      # 48

# def cite(author, quote):
#     print("{} said: {}".format(author, quote))


# cite('Bruce Eckel', 'Python is executable pseudocode.')
# # Bruce Eckel said: "Python is executable pseudocode."

# def squared_number(n):
#     return n**2

# print(squared_number(3))  # 9

# def multiples_of_three():
#     divisor = 1

#     for dividend in range(3, 31, 3):
#         print(f'{dividend} / {divisor} = 3')
#         divisor += 1

# multiples_of_three()

# function that compares the length of two strings
# It should return -1 if the first string is shorter
# 1 if the second string is shorter
# 0 if they're of equal length.

# def compare_by_length(text1, text2):
#     if len(text1) < len(text2):
#         return -1
#     elif len(text1) > len(text2):
#         return 1
#     else:
#         return 0


# compare_by_length('patience', 'perseverance') # -1
# compare_by_length('strength', 'dignity')      #  1
# compare_by_length('humor', 'grace')           #  0


 
# str1 = "    "
# str2 = "  Hello   "
# str3 = "Hello World"

# print(str1.isspace())
# print(str2.isspace())
# print(str3.isspace())

# sentence = "Hello     World!   How are you?   "
# word_count = sum(1 for word in sentence.split() if word.isspace())
# print("Number of words in the sentence:", word_count)

# Use string methods on the string 'Captain Ruby' 
# to create a string with the value 'Captain Python'

# import random

# code_list = ['en', 'fr', 'pt', 'de', 'sv', 'af']

# def greet():
#     random_choice = random.choice(code_list)

#     match random_choice:
#         case 'en':
#             return 'Hi!'
#         case 'fr':
#             return 'Salut!'
#         case 'pt':
#             return 'Ola!'
#         case 'de':
#             return 'Hallo!'
#         case 'sv':
#             return 'Hej!'
#         case 'af':
#             return 'Haai!'
        
#     return random_choice


# print(greet())       

# def extract_language(code):
#     # lang_prefix = code[:2]
#     # return lang_prefix

# def extract_region(locale):
#     # return locale[3:5]
#     return locale.split(".")[0].split("_")[1]

# print(extract_region('en_US.UTF-8'))    # US
# print(extract_region('en_GB.UTF-8'))    # GB
# print(extract_region('ko_KR.UTF-16'))   # KR


# passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

# new_passcode = '-'.join(passcode)

# print(new_passcode)

# Write some code here.
# Expected output: 11-jZ5-hQ3f*-8!7g3-p3Fs




# grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
#                 'carrots', 'broccoli', 'hummus']

# while grocery_list:
#     checked_item = grocery_list.pop(0)
#     print(checked_item)
    

# print(grocery_list)


# numbers = {
#     'high':   100,
#     'medium': 50,
#     'low':    25,
# }
# half_numbers = []
# for number in numbers.values():
#     half_numbers.append(number // 2)

# print(half_numbers)


# def outer():
#     def inner1():
#         def inner2():
#             foo = 3
#             print(f"inner2 -> {foo} with id {id(foo)}")

#         foo = 2
#         inner2()
#         print(f"inner1 -> {foo} with id {id(foo)}")

#     foo = 1
#     inner1()
#     print(f"outer -> {foo} with id {id(foo)}")

# outer()




# from copy import deepcopy as dc

# dict1 = {
#     'a': [[7, 1], ['aa', 'aaa']],
#     'b': ([3, 2], ['bb', 'bbb']),
# }

# dict2 = dc(dict1) 

# # All of these should print False
# print(dict1         is dict2)
# print(dict1['a']    is dict2['a'])
# print(dict1['a'][0] is dict2['a'][0])
# print(dict1['a'][1] is dict2['a'][1])
# print(dict1['b']    is dict2['b'])
# print(dict1['b'][0] is dict2['b'][0])
# print(dict1['b'][1] is dict2['b'][1])

# # All of these should print True

# print(dict1['a'][0][0] is dict2['a'][0][0])
# print(dict1['a'][0][1] is dict2['a'][0][1])
# print(dict1['a'][1][0] is dict2['a'][1][0])
# print(dict1['a'][1][1] is dict2['a'][1][1])
# print(dict1['b'][0][0] is dict2['b'][0][0])
# print(dict1['b'][0][1] is dict2['b'][0][1])
# print(dict1['b'][1][0] is dict2['b'][1][0])
# print(dict1['b'][1][1] is dict2['b'][1][1])





my_dict = {'a': 1, 'b': 2, 'c': 3}
for (key, value) in my_dict.items():
    print(f'{key} = {value}')
