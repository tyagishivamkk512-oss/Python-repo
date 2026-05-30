class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary


    @property
    def salary(self):                   
        return f"{self.name}'s monthly salary is ${self._salary}"
    
    @property
    def annual(self):                   
        return f"{self.name}'s annual salary is ${self._salary*12}"

    @salary.setter
    def salary(self, value):            
        if value < 0:
            print("Salary can't be negative!")
        else:
            self._salary = value

    @annual.deleter
    def annual(self):                  
        print(f"Deleting {self.name}'s salary...")
        del self._salary

e = Employee("Shivam", 50000)

print(e.annual)     
e.salary = 60000   
print(e.annual)      
del e.annual       
#print(e.annual)     