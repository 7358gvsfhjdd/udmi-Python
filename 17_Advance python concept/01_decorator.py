def decorator(func):
    def wrapper():
        print("I am about to execute a function....")
        func()
        print("I have executes this fuctions....")
    return wrapper
 
@decorator
def say_hello():
    print("Hello!")
    
say_hello()
#f = decorator (say_hello)
#f()

'''
f will look somerhing like this 
def f ()
print("I am about to execute a function....")
        func()
        print("I have executes this fuctions....")
'''