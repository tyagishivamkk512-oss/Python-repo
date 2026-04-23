# *args = allows to pass multiple non key arguments
  #  * = unpacking operator
def sum(*a):
    total=0
    for i in a:
        total+=i
    return total
print(sum(1,4,2,6,7))

# **kwargs = allows us to pass multiple key arguments
# class of args is tuple and kwargs is dictionary 

def address(**kwargs):
    print("Your address is: ")
    for key in kwargs.values():
        print(key, end=" ")

address(House_no="592",
        colony = "Indira Colony",
        city = "Muzaffarnagar")

