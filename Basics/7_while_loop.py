food = input("Enter a food you like (press x to quit): ")

while food != "x": #we can also use while not food == "x":
    print(f"Oh! so you like {food}")
    food=input("Enter another food you like (press x to quit): ")

print("Bye")

age = int(input("Please enter your age: "))

while age > 100 or age < 0:
    print("This is not your real age!")
    age = int(input("Please re-enter your age: "))

print(f"So youre {age} years old!")

# Fairly useful for verifying user input and if input is incorrect we can reprompt them
