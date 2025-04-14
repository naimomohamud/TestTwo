def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Call the function to print the first 10 Fibonacci numbers
fibonacci(10)
