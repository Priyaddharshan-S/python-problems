def remove_duplicate(lst):
    if not lst:
        return 'List is empty'
    non_duplicate = []
    for i in lst:
        if i not in non_duplicate:
            non_duplicate.append(i)

    return non_duplicate

lst = [1,2,2,2,3,4,56,66,66]
print(remove_duplicate(lst))