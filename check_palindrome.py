def str_rev(value):
    index = -1
    reversed = ''

    while(-len(value) <= index):
        reversed += value[index]
        index -= 1
    return reversed


def check_palindrome(value):
    rev = str_rev(value)

    if rev == value:
        return 'Palindrome'
    else:
        return 'Noa a palindrome'
    
print(check_palindrome("dad"))