def reverse_string(string):
    reversed_str = ""
    for char in string:
        reversed_str = char + reversed_str

    return reversed_str   


print(reverse_string("hello"))
print(reverse_string("hello") == "olleh")
