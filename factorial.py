def factorial(number, n=1):
    if number == 0 and n==1:
        return 0
    elif number >  0:
        n = n * number
        return factorial(number-1, n)
    else:
        return n

print(factorial(4))
print(factorial(3))
print(factorial(0))
