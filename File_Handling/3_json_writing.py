import json
employees = {"name":'Shivam',
             "age":"20",
             "job":"student"}

file_path = "python/file_handling/hello.json"

with open(file_path, "w") as file:
    json.dump(employees, file, indent=4)
    print(f"{file_path} created")
