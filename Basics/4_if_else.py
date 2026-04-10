age = int(input("Enter your age: "))

if age>=18:
    print("you are adult")
elif age<0:
    print("you are nothing")
else:
    print("you are Underage")


temp = int(input("temperature: ")) 

if temp<18 or temp>35:
    print("you should not go outside")
else: 
    print("you can go outside")

# similarly and and not can be used 

num = 5
print("Even" if num%2==0 else "Odd")
# X if "condition" else Y