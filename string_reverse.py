def str_rev(value):
    index = len(value) -1
    reversed = ''
    while(index >= 0):
        reversed  += value[index]
        index -= 1
    return reversed

print(str_rev("Priyaddharshan"))


