class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    #instance method
    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee("Shivam", "Manager")
employee2 = Employee("Tyagi", "Cashier")
employee3 = Employee("Bittu", "Cook")

print(Employee.is_valid_position("Rocket Scientist"))  
print(employee1.get_info())       

# instance is used when info is changed for every object
# static is used when info or criteria is same for each object                      