def fibonacci(index, counter=0, fib=[]):
    if index == 0 or index == 1:
        return index
    elif len(fib) == 0 or len(fib) == 1:
        fib.append(counter)
        return fibonacci(index, counter+1, fib)
    elif counter == index:
        new = fib[counter - 2] + fib[counter - 1]
        fib.append(new)
        return fib[index]
    else:
        new = fib[counter - 2] + fib[counter - 1]
        fib.append(new)
        return fibonacci(index, counter+1, fib)

print(fibonacci(1))
