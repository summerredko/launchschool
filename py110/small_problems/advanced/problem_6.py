# Implement a binary_search function that takes a list 
# and a search item as arguments, 
# and returns the index of the search item if found, 
# or -1 otherwise. 

# E:
# Input: list
# Output: string or integer

# D:
# List

# A:
# Take a list and an item to search for as an arguments.
# Retrieve the middle value from the data.
# If the middle value is equal to search item, stop the search.
# If the middle value is less than search item:
# Discard the lower half, including the middle value.
# Repeat the process from the top, using the upper half as the starting data.
# If the middle value is greater than search item, 
# do the same as the previous step, but with opposite halves.

# def binary_search(lst, search_item):
#     halfway = len(lst) // 2
#     if lst[halfway] == search_item:
#         return lst[halfway]
#     if lst[halfway] > search_item:
#         for i in range(len(lst[:halfway])):
#             if lst[i] == search_item:
#                 return lst[i]
#     for i in range(len(lst[halfway:])):
#         if lst[i] == search_item:
#             return lst[i]
    

def binary_search(lst, search_item):
    high = len(lst) - 1
    low = 0

    while low <= high:
        mid = low + (high - low) // 2
        if lst[mid] == search_item:
            return mid
        elif lst[mid] < search_item:
            low = mid + 1
        else:
            high = mid - 1

    return -1




# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']

print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)


