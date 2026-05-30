class Employee:
    company = "Google"          # class variable

    def __init__(self, name, salary):
        self.name = name        # instance variable
        self.salary = salary

    def get_info(self):         # INSTANCE METHOD
        print(f"{self.name} earns {self.salary}")

    @classmethod
    def get_company(cls):       # CLASS METHOD
        print(f"Company: {cls.company}")

    @staticmethod
    def is_valid_salary(salary):  # STATIC METHOD
        return salary > 0

e1 = Employee("Shivam", 50000)
e2 = Employee("Rahul", 60000)

e1.get_info()                        # Shivam earns 50000
e2.get_info()                        # Rahul earns 60000  ← different per object

Employee.get_company()               # Company: Google  ← same for all
e1.get_company()                     # Company: Google  ← same for all

Employee.is_valid_salary(50000)      # True  ← just a utility
Employee.is_valid_salary(-100)       # False