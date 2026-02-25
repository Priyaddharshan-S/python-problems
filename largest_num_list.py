def largest_number(lst):
    if not lst:
        return 'List is empty'
    large = lst[0]
    for i in lst:
        if i > large:
            large = i
    return large
lst = [11,2,13,4]
print(largest_number(lst))