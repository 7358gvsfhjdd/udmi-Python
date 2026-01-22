class Employee:
    
    def _init_(self, salary, name, bond):
        self.salary = salary #create an instance attributesof name salary and assign it with salary
        self.name = name
        self.bond = bond
        
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")
        
e1 = Employee(34000, "Sam G", 10)
print(e1.get_salary())
e1.get_info()