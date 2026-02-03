def very_slow_func():
    print("Something....")
    print("Something....")
    print("Something....")
    print("something....")
    print("Something....")
    return 70

#a = very_slow_func()
#if (a>10):
#    print(a)

if ((a:=very_slow_func())>10):
    print(a)    
          
else:
    print("Its not greater than 10")