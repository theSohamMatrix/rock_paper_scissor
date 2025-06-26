# Rock, Paper & Scissor Game ...
'''
Choices for computer: 
1 Rock    = 1 
2 Paper   = 0
3 Scissor = -1
'''

import random

while True:
    # Header of game
    print("=" * 50)
    print("Rock Paper & Scissor Game".center(50))
    print("=" * 50)

    # User choices
    print('''Choose from this options: 
      1- Rock    : R
      2- Paper   : P
      3- Scissor : S
    ''')

    # Computer randomly selects choice
    computer = random.choice([1, 0, -1])
    c = computer

    # Valid input check
    valid_choices = ["R", "P", "S"]
    user = input("Enter your choice (R/P/S): ").upper()

    while user not in valid_choices:
        print("❌ Invalid input, please choose only from R, P, or S.")
        user = input("Enter your choice (R/P/S): ").upper()

    # Mapping for display
    choice_l_for_c = {1: "Rock", 0: "Paper", -1: "Scissor"}
    choice_l_for_u = {"R": "Rock", "P": "Paper", "S": "Scissor"}

    # Display selections
    print()
    print(f"Computer chose : {choice_l_for_c[c]}".center(50))
    print(f"You chose     : {choice_l_for_u[user]}".center(50))
    print("=" * 50)

    # Game logic
    if (c == 1 and user == "R") or (c == 0 and user == "P") or (c == -1 and user == "S"):
        print("It's A Draw!!".center(50))
    elif (c == 1 and user == "P") or (c == 0 and user == "S") or (c == -1 and user == "R"):
        print("🎉 You Win!!".center(50))
    else:
        print("😢 You Lost!!".center(50))

    print("=" * 50)

    # Play again prompt
    print("Y : Yes\nN : No")
    play_again = input("Do you want to play again (Y/N): ").upper()

    while play_again not in ["Y", "N"]:
        play_again = input("Please enter only Y or N: ").upper()

    if play_again == "N":
        print("\nThanks for playing!".center(50))
        break  # Exit the game loop

