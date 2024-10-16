import random 

while True:
    user_action = input("Enter a choice(rock paper sissors):")
    
    possible_action = ["rock", "paper", "sissors"]
    computer action = random_choice(possible_action)
{computer_action}.\n") 


    if user_action == computer_action:
        print(f"both player selected{user_action}. its a tie!")
    elif user_action == "rock"
        if computer_action == "sissors":
             print("Rock smashes the sissor! you win!!")
        else:
             print("Paper covers the rock!you lose!!")
     elif user_action == "paper"
        if computer_action == "rock":
             print("Rock smashes the sissor! you win!!")
        else:
             print("sissors cut the paper!you lose!!")
     elif user_action == "sissors"
        if computer_action == "paper":
             print("sissors cuts paper! you win!!")
        else:
             print("Paper covers the rock!you lose!!")
     elif user_action == "rock"
        if computer_action == "sissors":
             print("Rock smashes the sissor! you win!!")
        else:
             print("Paper covers the rock!you lose!!")
 play_again = input("play again? (y/n):")
 if play_again != "y"
    break