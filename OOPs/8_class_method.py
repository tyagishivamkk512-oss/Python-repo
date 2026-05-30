class student:
    count = 0
    totalcg = 0

    def __init__ (self, name, cg):
        self.name = name
        self.cg = cg
        student.count += 1
        student.totalcg += cg

    def data(self):
        return f"{self.name} = {self.cg} cgpa"
    
    @classmethod
    def total(cls):
        print(f"total students are {cls.count:.2f}")

    @classmethod
    def meancg(cls):
        if cls.count == 0:
            return 0
        else:
            return f"mean cgpa is :{cls.totalcg/cls.count}"


s1 = student('shivam', 10)
s2 = student('tyagi', 9)

student.total()
print(s1.data())
print(s2.data())
print(student.meancg())

#Class method is for data that belongs to the whole class, not any single object.