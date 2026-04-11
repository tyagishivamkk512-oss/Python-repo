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

#n[start:end:step]

#print(n[1:6])  print from index 1 to 5 
#print(n[4:])  print from index 4 to end
#print(n[:6])  print from index 0 to 5 
#print(n[-1])  print last digit basically reverse index
print(n[::2]) #will print whole n by gap of 2