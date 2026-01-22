class Animal:
    def __init__(self, name):
        self.name = name 
    def speak(self):
        print("Generic animal sound")
    
class Dog(Animal):
    def speak(self):
        print("Woof!")    
        
a = Animal("Dog")
a.speak()