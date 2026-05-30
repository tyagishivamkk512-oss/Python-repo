from abc import ABC, abstractmethod

class shape:

    @abstractmethod
    def area(self):
        pass

class square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius
    
class pizza(circle):
    def __init__(self, radius, topping):
        super().__init__(radius)
        self.topping = topping
    

shapes = [circle(5), square(7), pizza(10, 'mushroom')]

for i in shapes:
    print(i.area())


        