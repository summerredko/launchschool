def multiply_list(lst):
    # new_lst = []
    # for item in lst:
    #     new_lst.append(item * 2)

    # return new_lst
    return [item * 2 for item in lst]

print(multiply_list([1, 2, 3]))
print(multiply_list([1, 2, 3]) == [2, 4, 6])
