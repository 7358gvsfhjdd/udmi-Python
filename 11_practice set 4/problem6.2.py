def fibonacci(n):
    """Recursive function to calculate the nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci(n):
    """Print the first n Fibonacci numbers"""
    print(f"First {n} Fibonacci numbers:")
    for i in range(n):
        print(fibonacci(i), end=" ")
    print()

# Example usage
if __name__ == "__main__":
    print_fibonacci(10)