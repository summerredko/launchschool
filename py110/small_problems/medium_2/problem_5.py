# def next_featured(num):
#     def has_unique_digits(n):
#         return len(set(n)) == len(n)

#     multiples7 = [i * 7 for i in range(num)]

#     multiples_over_num = [str(sevens) for sevens in multiples7 
#                           if sevens > num and sevens % 2 != 0]
    
#     multiples_single_digits = []
#     for digits in multiples_over_num:
#         if has_unique_digits(digits):
#             multiples_single_digits.append(int(digits))
    
#     if multiples_single_digits:
#         return multiples_single_digits[0]
#     else:
#         return "There is no possible number that fulfills those requirements."

# def to_odd_multiple_of_7(number):
#     number += 1
#     while number % 2 == 0 or number % 7 != 0:
#         number += 1

#     return number

# def all_unique(number):
#     digits = list(str(number))
#     return len(digits) == len(set(digits))

# def next_featured(number):
#     MAX_FEATURED = 9876543201
#     featured_num = to_odd_multiple_of_7(number)

#     while featured_num <= MAX_FEATURED:
#         if all_unique(featured_num):
#             return featured_num

#         featured_num += 14

#     return "There is no possible number that fulfills those requirements."


error = "There is no possible number that fulfills those requirements."

def repeats(num):
    return len(list(str(num))) != len(set(str(num)))

def next_featured(num):
    num += 1
    while num < 9876543201:
        while num % 7 != 0 or num % 2 == 0 or repeats(num) :
            num += 1
        return num
    return error

# Test cases
print(next_featured(12))                  # 21
print(next_featured(20))                  # 21
print(next_featured(21))                  # 35
print(next_featured(997))                 # 1029
print(next_featured(1029))                # 1043
print(next_featured(999999))              # 1023547
print(next_featured(999999987))           # 1023456987
print(next_featured(9876543186))          # 9876543201
print(next_featured(9876543200))          # 9876543201

error = "There is no possible number that fulfills those requirements."
print(next_featured(9876543201) == error) # True
