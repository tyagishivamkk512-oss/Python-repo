class animal:
    alive = True

class dog(animal):
    speak = "woof"

class cat(animal):
    speak = 'meow'

class car:
    speak = 'honk'
    alive = 'false'

animals = [dog(),cat(),car()]

for i in animals:
    print(i.speak)

# if a class behaves just like the other two then it can be considered same as the others 