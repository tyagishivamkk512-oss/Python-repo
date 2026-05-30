class student:

    class_year = 2026 #class variable
    num = 0
    def __init__(self, name, age, grade, roll_no):
        self.name = name
        self.age = age
        self.grade = grade
        self.roll_no = roll_no
        student.num+=1

    def remark(self):
        print(f"Very well {self.name}")

    def shout(self):
        print(f"Shut up {self.name}")

    # or we can make class in seperate file and import it here 

s1 = student("Shivam",20,'S',130)
s2 = student("Marcus",19,'B',100)
s3 = student("Harshit",23,'A',31)

# print(s1)  will print address of s1

s1.remark()
s2.shout()

print(s1.roll_no)
print(s2.class_year)
print(student.class_year)
print(student.num) #will give total students


