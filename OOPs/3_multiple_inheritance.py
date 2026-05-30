# multiple inheritance = inherits from more than one parent class
#                        C(A,B)
#multilevel inheritance = one inherites from other, other inherites from another
#                        C(B) <- B(A) <- A   

class animal:
    def __init__(self,name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

class prey(animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class predator(animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class rabbit(prey):
    pass

class hawk(predator):
    pass

class wolf(prey,predator):
    pass

rabbit1 = rabbit("bunny")
hawk1 = hawk("mugen")
wolf1 = wolf("spear")

wolf1.eat()
wolf1.hunt()
rabbit1.flee()
hawk1.hunt()