import random 
playing = True
number = str(random.randint(10,20))

print("I will generatea number from 0, to 9, and you have guess the number one digit at a time.")
print("The game ends when you get 1 hero!")
while playing:
    guess = input("Give me your best guess")
    if number == guess:
        print("you win the game")
        print("the number was", number)
        break
    
    
    else:
        print("Your guess isnt quite right, try again")
    
