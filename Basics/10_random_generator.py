import random

number = random.randint(1,100) # generate random number between 1 to 100
number = random.random() # generates random float number

option = {'a','b','c','d'}
random.choices(option) # will select random from option
random.shuffle(option) #will shuffle options

# random.choice will select one
# random.choices(list, k=4) will select 4 
# random.sample(list, 4) will select 4 
