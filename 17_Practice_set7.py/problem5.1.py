class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a number: "))
    
    if num<0:
        raise NegativeNumberError("Number is negative")
    
    result = 45/num
    print(f"The result is {result}")
    
except ValueError:
    print("Error: Please enter a proper number")
    
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
    
except NegativeNumberError as e:
    print(f"Error: {e}", e)