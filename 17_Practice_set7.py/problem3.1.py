class Mathutils:
    def __init__(self):
        pass
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def description(cls):
        print("this is a utility class for math operations. ")
        
a = Mathutils
print(a.add(5,34))
a.description()

#MathUtils.description(
#print(MathUtils.add(5, 34))