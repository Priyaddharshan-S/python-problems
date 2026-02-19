def swap_num(num1, num2):
    num1, num2 = num2, num1
    return num1,num2

num1, num2 = swap_num(5,7)
print(num1, num2)