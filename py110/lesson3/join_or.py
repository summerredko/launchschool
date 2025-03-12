# Input: lists and strings
# Output: string



def join_or(lst, delimiter=', ', conjunction='or'):
    if len(lst) == 1:
        return str(lst[0])
    elif len(lst) == 2:
        return str(lst[0]) + ' or ' + str(lst[1])
    elif len(lst) == 0:
        return ""
    
    result = ""
    for i in range(len(lst) - 1): 
        result += str(lst[i])
        if i < len(lst) - 1:  
            result += delimiter

    result += conjunction + " "
    result += str(lst[-1])

    return result




print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"
