data = "mai shivam hun"
employees = ["Shivam","harshit",'khiladi', 'conor'] 

file_path = "python/file_handling/text.txt"

with open(file_path, "w") as file:
    for employee in employees:
        file.write(employee + "\n")
    print(f"{file_path} created")

# using "a" in place of "w" will type same text again like mai shivam hunmai shivam hun
# using "x" will create file but will give error if already exists while "w" overwrites