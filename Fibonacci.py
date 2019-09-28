def fib():
    count = int(input("Enter the number fib you want to print out : "))
    print("You have enter: ", count)
    i = 1
    if count == 0:
        fib = [0]
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while i < count - 1:

            fib.append((fib[i] + fib[i-1]))
            i += 1
    return fib
print("your fibonacci number is:", fib())