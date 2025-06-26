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

user = input("Enter Your Choice: ").upper()


choice_l_for_c = {1 : "Rock",0 : "Paper",-1 : "Scissor"} 
choice_l_for_u = {"R": "Rock", "P": "Paper", "S" : "Scissor"}

# Display what is choosed by user and computer: 
print("")
print(f"Computer choosed : {choice_l_for_c[c]}".center(50))
print(f"You choosed: {choice_l_for_u[user]}".center(50))
print("="*50 )

# game system: 
if(c== 1 and user == "R"):  # for a draw
    print("Its A Draw!!".center(50))
elif(c== 0 and user == "P"): 
    print("Its A Draw!!".center(50))
elif(c== -1 and user == "S"): 
    print("Its A Draw!!".center(50))
elif(c== 1 and user == "P"): # for rock(c)
    print("You Win!!")
elif(c== 1 and user =="S"):
    print("You Loosed!!".center(50))
elif(c==0 and user == "R"): # for paper(c)
    print("You Loosed!!".center(50))
elif(c==0 and user == "S"):
    print("You Win!!".center(50))
elif(c==-1 and user == "R"): # for scissor(c)
    print("You Win!!".center(50))
elif(c==-1 and user == "P"):
    print("You Loosed!!".center(50))
else: 
    print("Something Went Wrong")
print("="*50 )
    
print("Thank you for playing".center(50))