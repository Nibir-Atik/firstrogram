def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)

def generate_fibonacci(nterms):
    if nterms <= 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        fib_sequence = [str(recur_fibo(i)) for i in range(nterms)]
        print(", ".join(fib_sequence))

# Example usage
generate_fibonacci(15)