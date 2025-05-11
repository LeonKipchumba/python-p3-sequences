def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    
    fibonacci = [0]
    if length == 1:
        print(fibonacci)
        return
    
    fibonacci.append(1)
    for i in range(2, length):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    
    print(fibonacci)