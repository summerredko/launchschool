#1 
# for i in range(10):
#     hyphen = "-" * i
#     print(f'{hyphen}The Flintstones Rock!')

#2 
# def factors(number):
#     divisor = number
#     result = []
#     while divisor > 0:
#         if number % divisor == 0:
#             result.append(number // divisor)
#         divisor -= 1
#     return result

#3 The second function creates a new buffer
# def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
#     buffer.append(new_element)
#     if len(buffer) > max_buffer_size:
#         buffer.pop(0)
#     return buffer

# def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
#     buffer = buffer + [new_element]
#     if len(buffer) > max_buffer_size:
#         buffer.pop(0)
#     return buffer

#4 Ouputs 0.8999999999999999 and False without math.isclose function
# print(0.3 + 0.6)
# print(0.3 + 0.6 == 0.9)

#5 Returns False without the math.isnan function
# import math

# nan_value = float("nan")

# print(math.isnan(nan_value))

#6 Outputs 34
# answer = 42

# def mess_with_it(some_number):
#     return some_number + 8

# new_answer = mess_with_it(answer)

# print(answer - 8)

#7 The dictionary is mutated
# munsters = {
#     "Herman": {"age": 32, "gender": "male"},
#     "Lily": {"age": 30, "gender": "female"},
#     "Grandpa": {"age": 402, "gender": "male"},
#     "Eddie": {"age": 10, "gender": "male"},
#     "Marilyn": {"age": 23, "gender": "female"},
# }

# def mess_with_demographics(demo_dict):
#     for key, value in demo_dict.items():
#         value["age"] += 42
#         value["gender"] = "other"

#8 Returns paper
# def rps(fist1, fist2):
#     if fist1 == "rock":
#         return "paper" if fist2 == "paper" else "rock"
#     elif fist1 == "paper":
#         return "scissors" if fist2 == "scissors" else "paper"
#     else:
#         return "rock" if fist2 == "rock" else "scissors"
    
# rps("rock", "paper") # paper
# rps("rock", "scissors") # rock (returns paper, rock)
# rps("paper", "rock") # paper
    
# print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

#9 Returns False due to the foo() function returning yes
# def foo(param="no"):
#     return "yes"

# def bar(param="no"):
#     return (param == "no") and (foo() or "no")

# print(bar(foo()))

#10 Outputs as true due to referencing shared object
# a = 42
# b = 42
# c = a

# print(id(a) == id(b) == id(c))
