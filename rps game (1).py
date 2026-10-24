import random

computer = ("rock", "paper", "scissors")  

while True:  
    computer_choice = random.choice(computer)
    User = input("Enter your choice (rock/paper/scissors)\n\t:=").lower()  

    if (User == computer_choice):
        print("Match tie ,Try again!")

    elif ("rock" in User and "scissors" in computer_choice):
        print("----<You Win>----")

    elif ("rock" in computer_choice and "scissors" in User):
        print("---<You lose!>---")

    elif ("scissors" in User and "paper" in computer_choice):
        print("----<You Win>----")

    elif ("scissors" in computer_choice and "paper" in User):
        print("---<You lose!>---")

    elif ("paper" in User and "rock" in computer_choice):
        print("---<You Win >---")

    elif ("paper" in computer_choice and "rock" in User):
        print("---<You lose!>---")

    else:  
        print("Invalid input! Please type rock, paper, or scissors.")

    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing!")
        break
