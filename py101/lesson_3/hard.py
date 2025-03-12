#1 The second() function returns None
# def first():
#     return {
#         'prop1': "hi there",
#     }

# def second():
#     return
#     {
#         'prop1': "hi there",
#     }

# print(first())
# print(second())

#2
# dictionary = {'first': [1]}
# num_list = dictionary['first']
# num_list.append(2)

# print(num_list) # Outputs 'first': [1, 2]
# print(dictionary) # Outputs 'first': [1, 2]

#3a Outputs one, two, three
# def mess_with_vars(one, two, three):
#     one = two
#     two = three
#     three = one

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}")
# print(f"two is: {two}")
# print(f"three is: {three}")

#3b Outputs one, two, three
# def mess_with_vars(one, two, three):
#     one = ["two"]
#     two = ["three"]
#     three = ["one"]

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}")
# print(f"two is: {two}")
# print(f"three is: {three}")

# #3c Outputs two, three, one
# def mess_with_vars(one, two, three):
#     one[0] = "two"
#     two[0] = "three"
#     three[0] = "one"

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}")
# print(f"two is: {two}")
# print(f"three is: {three}")

#4
# def is_an_ip_number(str):
#     if str.isdigit():
#         number = int(str)
#         return 0 <= number <= 255
#     return False

# def is_dot_separated_ip_address(input_string):
#     dot_separated_words = input_string.split(".")
#     if len(dot_separated_words) != 4:
#         return False

#     while dot_separated_words:
#         word = dot_separated_words.pop()
#         if not is_an_ip_number(word):
#             return False

#     return True

# print(is_dot_separated_ip_address("word"))
# print(is_an_ip_number("10.4.5.11"))

#5 Return a NameError
# if False:
#     greeting = "hello world"

# print(greeting)

