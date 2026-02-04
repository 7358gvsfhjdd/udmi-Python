def fun1(*args, **kwargs):
    print(args)
    print(kwargs)
    
fun1(1, 2, 3, 5, jack = 34, jill = 45, marie=31)