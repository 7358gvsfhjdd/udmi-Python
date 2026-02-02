numbers = [ 1, 2, 3, 45, 4, 21]

def square (x):
    return x * x

new = list (map(square,numbers))
print(new)