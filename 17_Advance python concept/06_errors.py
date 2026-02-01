while True:
    try:
        a = int (input("Enter a number 1: "))
        b = int (input("Enter a number 2: "))
        print(f"The division is {a/b}")
        
    except ValueError:
        print("print dont perform bed typecast")
        
    except ZeroDivisionError:
        print("Hey dont dibvide by 0")
        
    except Exception as e:
        print ("Unknown error occoured!", e)