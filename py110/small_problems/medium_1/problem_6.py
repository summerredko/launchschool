# P:
# Determine if a number if prime 
# (not divisible by another number other than itself and 1)

# E:
# Write a function that takes a positive integer as an argument 
# and returns a Boolean value

# D:
# Integers

# A:
# Take an integer as an argument.
# Use modulo to check if that number if divisible 
# If so, return False
# If not, return True

# prime number
# check if the number is divisable by any prime number less <= it's square root



def is_prime(number):
    if number == 1:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True

print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True
