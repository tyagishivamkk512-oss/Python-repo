class shape:
    def __init__(self,colour, isfilled):
        self.colour = colour
        self.isfilled = True

    def describe(self):
        print(f"it is {self.colour} and {'filled' if self.isfilled else 'not filled'}")


class square(shape):
    def __init__(self, colour, isfilled, side):
        super().__init__(colour, isfilled)
        self.side = side

    def describe(self):
        print("It is a square!!")
        super().describe()

class circle(shape):
    def __init__(self, colour, isfilled, radius):
        super().__init__(colour, isfilled)
        self.radius = radius

    def describe(self):
        super().describe()
        print("It is a circle!!")
    

circle1 = circle('red',False,5)
square1 = square('blue',True,7)

circle1.describe()
print(f"{square1.side}cm")
square1.describe()
        