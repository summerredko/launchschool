# P:
# Write a function that takes a string and returns a dictionary evaluating the percentage of lowercase, uppercase and neither characters.

# E:
# Percentages should round to two decimal points.

# D:
# Dictionary
# String

# A:
# Create a dictionary with the key names: lowercase, uppercase, neither
# Take in a string as an argument.
# Count the length of string and store into LENGTH
# Create variables for LOWERCASE, UPPERCASE, NEITHER
# Loop over the string.
# If char is lowercase, increase LOWERCASE count by 1
# If char is uppercase, increase UPPERCASE count by 1
# If char is neither, increase NEITHER count by 1
# Retrieve percentage break down of each variable by dividing their count by LENGTH
# Round to two decimals
# Add that value to dictionary


def letter_percentages(string):

    char_counts = {
    "lowercase": "",
    "uppercase": "",
    "neither": "",
    }
    
    length = len(string)
    lowercase_count = 0
    uppercase_count = 0
    neither_count = 0
    for char in string:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        else:
            neither_count += 1

    char_counts["lowercase"] = f"{round((lowercase_count / length) * 100, 2):.2f}"
    char_counts["uppercase"] = f"{round((uppercase_count / length) * 100, 2):.2f}"
    char_counts["neither"] = f"{round((neither_count / length) * 100, 2):.2f}"

    return char_counts


expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)
