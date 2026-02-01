def divide(a, b):
    try:
        c = a/b
        print(c)
        return c
    except  Exception as e:
        print(e)
        return None 
    #This is always executes no matters if try completly executes or not 
    finally:
        print ("This is always executed")
        
a = int(input("Enter nimber 1: "))
b = int(input("Enter number2: "))
divide(a,b)