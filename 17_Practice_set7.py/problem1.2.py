from time import time

def timer(func):
    def wrapper(n):
        t1 = time()
        result =func(n)
        t2 = time()
        print(t2 - t1)
        return result 
    return wrapper

@timer
def sum_1m(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

a = sum_1m(1000000)
print(a)