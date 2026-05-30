class animal:
    def __init__(self,name,food):
        self.name = name
        self.is_alive = True
        self.is_animal = True # same for every one so no need to pass as an argument
        self.food = food

    def sleep(self):
        print(f"{self.name} is sleeping")

class dog(animal):
    def speak(self):
        print("Bhauu")

class cat(animal):
    def speak(self):
        print("myauu")

class mouse(animal):
    def speak(self):
        print("choon choon")

dog1 = dog('Dharmendar','roti')
cat1 = cat('neko','milk')
mouse1 = mouse('mithu','cheese')

print(dog1.name)
print(dog1.is_alive)
print(cat1.food)
mouse1.sleep()
mouse1.speak()

    