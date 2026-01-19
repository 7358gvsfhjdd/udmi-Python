def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(5, 0))   # Output: Cannot divide by zero
