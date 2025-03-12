# # fruits = {'apple': 3, 'banana': 2, 'orange': 5, 'pear': 1}

# # print(list(fruits.keys()))      # ['apple, 'banana', 'orange', 'pear']
# # print(list(fruits.values()))    # [3, 2, 5, 1]
# # print(list(fruits.items()))     # [('apple, 3), (banana', 2), ('orange', 5), ('pear', 1)]
# # print(fruits.get('grape', 0))   # 0
# # print(fruits.get('apple', 0))   # 3

# my_dict = {
#     'a': 'abc',
#     37: 'def',
#     (5, 6, 7): 'ghi',
#     frozenset([1, 2]): 'jkl',
# }

# my_dict['a'] = 'ABC'
# my_dict[37] = 'DEF'
# my_dict[(5, 6, 7)] = 'GHI'
# my_dict[frozenset([1, 2])] = 'JKL'
# # print(my_dict)

# my_dict['xyz'] = 'Hey there!'
# my_dict[[1, 2, 3]] = 'Hey there!'
# print(my_dict)         


# x = "global"

# def outer():
#     x = "outer"
    
#     def inner():
#         x = "inner"
#         print("Inner x:", x)
        
#         def innermost():
#             print("Innermost x:", x)
        
#         innermost()
    
#     inner()
#     print("Outer x:", x)

# outer()
# print("Global x:", x)




# Executes the program how Python does it in real time
# Python -m trace -t yourscript.py



# Strings are not mutable:
# def modify_string(text):
#     text = text.upper()
#     return text

# message = 'hello world'
# message = modify_string(message)
# print(message)





# def modify_list(lst):
#     lst.append(4)
#     lst = [1, 2, 3]
#     return lst

# numbers = [0]
# result = modify_list(numbers)
# print(numbers)  # [0, 4]
# print(result)   # [1, 2, 3]



# def modify_dict(d):
#     d['b'] = 2
#     d = {'c': 3}
#     return d

# my_dict = {'a': 1}
# result = modify_dict(my_dict)
# print(my_dict) # {'a': 1, 'b': 2}
# print(result)   # {'c': 3}





letters = ['a', 'b', 'c', 'd']

# def reverse_list1(lst):
#     return lst[::-1]

# def reverse_list2(lst):
#     return lst.reverse()

# print(reverse_list1(letters))   
# print(reverse_list2(letters))
# print(letters)                  




# players = [
#   {'name': "Joe", 'age': 25}, 
#   {'name': "Andy", 'age': 31}, 
#   {'name': "Ralph", 'age': 18}, 
#   {'name': "Mark", 'age': 28},
# ]

# new_team = players
# last_years_team = players[:]

# new_team.append({
#     'name': 'Bob',
#     'age': 19,
# })

# def age_players(players):
#     for player in players:
#         player['age'] += 1

# age_players(players)

# print(players)
# print()
# print(new_team)
# print()
# print(last_years_team)
