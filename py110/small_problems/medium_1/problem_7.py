# (n - 1) + F(n - 2)
# 1 + 1 = 2
# 2 + 3 = 5
# 3 + 5 = 8...

def fibonacci(nth):
    if nth <= 2:
        return 1

    previous, current = 1, 1
    for _ in range(3, nth + 1):
        previous, current = current, previous + current

    return current    


print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True
