def decrease(count):
    return count - 1

counter = 10

for _ in range(10):
    print(counter)
    counter = decrease(counter)

print('LAUNCH!')
