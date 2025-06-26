# Rock, Paper & Scissor Game ...
'''
Choices for computer: 
1 Rock = 1 
2 Paper = 0
3 Scissor = -1
'''
import random
# Header of game
print("="*50)
print("Rock Paper & Scissor Game".center(50))
print("="*50)

# User choices: 
print('''Choose from this options: 
      1- Rock    : R
      2- Paper   : P
      3- Scissor : S
      '''
)
# Taking Inputs from user & sorting
computer = random.choice([1,0,-1])
c = computer

user = input("Enter Your Choice: ").upper
you = user

choice_l_for_c = {1 : "Rock",0 : "Paper",-1 : "Scissor"} 
choice_l_for_u = {"R": 1, "P": 0, "S" : -1 }

# Display what is choosed by user and computer: 
print(f"Computer choosed : {choice_l_for_c[c]}\nYou choosed: {choice_l_for_u[you]}")

