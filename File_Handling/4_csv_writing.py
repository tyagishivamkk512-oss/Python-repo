import csv
employees = [['name','age','job'],
             ['shivam','20','student'],
             ['conor','64','labourer'],
             ['satpal','32','unemployed']]

file_path = "python/file_handling/new.csv"

with open(file_path, "w") as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)
    print(f"{file_path} created")
