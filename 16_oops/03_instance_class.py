class Employee:
    company =  "Asus"
    
    def _init_(self, salary, name, bond, company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company
    
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} year")
    
e1 = Employee(4000, "Sam", 10, "Tesla")
print(e1.company) #It will aways print instance attributes whenever its present
