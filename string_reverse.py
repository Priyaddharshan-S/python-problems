def str_rev(value):
    index = -1
    reversed = ''
    while(-len(value) <= index):
        reversed  += value[index]
        index -= 1
    return reversed

print(str_rev("Priyaddharshan"))


