name = "Shivam Tyagi"

result = len(name) # will give no. of characters
result = name.find("m") #will give index at which m is
                        # rfind() will return -1 if the character does not exist

name = name.upper() # make name to all uppercase
name = name.lower()
name = name.capitalize() # will make first letter capital
result = name.isalpha() # if there are only alphabets will return true otherwise false
result = name.isdigit()


number = "898985454545"
print(number.count("5")) # will count no. of 5 but only works if number is string
number = number.replace("9","7") #will replace 9 with 7

n = "1234567890"
print(n[1:6])