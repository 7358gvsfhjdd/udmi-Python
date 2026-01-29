class Student:
    def __init__(self, age):
        self.__age = age

    # Getter
    @property
    def age(self):
        return self.__age

    # Setter
    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            print("Invalid age")
