# procedure bubbleSort(A : list of sortable items)
#     n := length(A)
#     repeat
#         swapped := false
#         for i := 1 to n-1 inclusive do
#             { if this pair is out of order }
#             if A[i-1] > A[i] then
#                 { swap them and remember something changed }
#                 swap(A[i-1], A[i])
#                 swapped := true
#             end if
#         end for
#     until not swapped
# end procedure

def bubble_sort(lst):
    n = len(lst)
    while True:
        swapped = False
        for i in range(n-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True
        if not swapped:
            break
    return lst
        

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True
