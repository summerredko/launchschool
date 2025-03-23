# NUMBERS = {
#     "zero": 0,
#     "one": 1, 
#     "two": 2,
#     "three": 3,
#     "four": 4,
#     "five": 5,
#     "six": 6,
#     "seven": 7,
#     "eight": 8,
#     "nine": 9,
# }

# def word_to_digit(string):
#     new_string = ""
#     for word in string.split():
#         if word not in NUMBERS:
#             new_string += word + " "
#         if word in NUMBERS:
#             new_string += str(NUMBERS[word]) + " "
   
#     return new_string[:-1]

import string

NUM_WORDS = {
    'zero':  '0',
    'one':   '1',
    'two':   '2',
    'three': '3',
    'four':  '4',
    'five':  '5',
    'six':   '6',
    'seven': '7',
    'eight': '8',
    'nine':  '9',
}

def word_to_digit(sentence):
    words = sentence.split()
    processed_words = []

    for word in words:
        # Remove punctuation from the word
        clean_word = word.strip(string.punctuation)
        # Convert word to digit if it exists in NUM_WORDS
        digit = NUM_WORDS.get(clean_word, clean_word)
        # Preserve the original punctuation
        if word[-1] in string.punctuation:
            digit += word[-1]
        processed_words.append(digit)

    return ' '.join(processed_words)


message = 'Please call me at five five five one two three four!'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
print(word_to_digit(message))
# Should print True
