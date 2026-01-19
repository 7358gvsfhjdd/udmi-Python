def sum(a, b):
    # a and b are local variables
    c = a + b
    z = 1 # It create local variable Z
   # print(z)# z is a global vRIble
    return c

z = 10
print (sum(6,4))
print(z)