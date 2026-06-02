import os 

file_path = 'hello.txt'
if os.path.exists(file_path):
    print("It exists") 
    if os.path.isfile(file_path):
        print("it is a file")
    elif os.path.isdir(file_path):
        print("it is a directory")

else:
    print("it does not exist")
