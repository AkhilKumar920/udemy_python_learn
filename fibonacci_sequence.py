def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = generate_fibonacci(n)
print(f"Fibonacci Sequence for {n} numbers: {fib_sequence}")
