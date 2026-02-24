def prime_intervals(num1, num2):
    for num in range(num1, num2 + 1):
        if num <= 1:
            continue
        
        prime = True   # Reset for every number
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        
        if prime:
            print(num)

prime_intervals(1, 10)