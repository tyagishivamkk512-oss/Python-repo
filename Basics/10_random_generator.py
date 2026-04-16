import random

number = random.randint(1,100) # generate random number between 1 to 100
number = random.random() # generates random float number

option = {'a','b','c','d'}
random.choices(option) # will select random from option
random.shuffle(option) #will shuffle options
