a = int (input("Enter a number 1: "))
b = int (input("Enter a number 2: "))

if b == 0:
    raise ValueError("Please not divide by 0")

print(f"The division is {a/b}")