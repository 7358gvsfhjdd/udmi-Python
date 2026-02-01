a = int (input("Enter a number 1: "))
b = int (input("Enter a number 2: "))

try:
    c = a/b
    print(c)
    
except Exception as e:
    print(e)
    
#these is always executed no matter if trh completly executes or not 

finally:
    print("This is always executed")