import random
option = ['rock','paper','scissor']

player = None
computer = random.choice(option)

while player not in option:
    player = input("Enter (rock/paper/scissor): ")

print(f"Computer has choosen: {computer}")
    
if player == computer:
    print("It's a TIE!!")

elif ((player == 'rock' and computer== 'scissor') or 
    (computer == 'paper' and player== 'scissor') or  
    (player == 'paper' and computer== 'rock')):
    print("You've WON!!")

elif ((computer == 'rock' and player== 'scissor') or 
    (player == 'paper' and computer== 'scissor') or 
    (computer == 'paper' and player== 'rock')):
    print("You've LOST!!")

