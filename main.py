print("Welcome to the game of Rock, Paper, Scissors.")
print()
print()
print("RULES OF THE GAME")
print()
print("1. Rock defeats scissors, but it is defeated by paper.")
print("2. Paper defeats rock, but it is defeated by scissors.")
print("3. Scissors defeats paper, but it is defeated by rock.")
print()
print()
print("Are you ready to play?")
print()

import random

while True:
    print()
    R = "rock"
    P = "paper"
    S = "scissors"
    choice = [R, P, S]
    choice2 = ["R","P","S"]
    computer = random.choice(choice)
    user = None
    
    user = input("Choose either R for rock, P for paper or S for scissors: ").upper()
    while user not in choice2:
        print ("Error!!! Make sure you input R for rock, P for paper or S for scissors")
        print()
        user = input("Choose either R for rock, P for paper or S for scissors: ").upper()
    print()
    
 

    
    if user == "R":
        if computer == S:
            print("You chose: Rock")
            print("Computer chose: " + computer)
            print()
            print("You won!!! Congratulations.")
        if computer == P:
            print("You chose: Rock")
            print("Computer chose: " + computer)
            print()
            print("You lose!!! Better luck next time.")
        if computer == R:
            print("You chose: Rock")
            print("Computer chose: " + computer)
            print()
            print("Tie!!!")

    elif user == "P":
        if computer == S:
            print("You chose: Paper")
            print("Computer chose: " + computer)
            print()
            print("You lose!!! Better luck next time.")
        if computer == R:
            print("You chose: Paper")
            print("Computer chose: " + computer)
            print()
            print("You won!!! Congratulations.")
        if computer == P:
            print("You chose: Paper")
            print("Computer chose: " + computer)
            print()
            print("Tie!!!")

    elif user == "S":
        if computer == R:
            print("You chose: Scissors")
            print("Computer chose: " + computer)
            print()
            print("You lose!!! Better luck next time.")
        if computer == P:
            print("You chose: Scissors")
            print("Computer chose: " + computer)
            print()
            print("You won!!! Congratulations.")
        if computer == S:
            print("You chose: Scissors")
            print("Computer chose: " + computer)
            print()
            print("Tie!!!")
    print()

    play_again = input("Would you like to play again? (yes or no): ").lower()
    if play_again != "yes":
        break
print()
print("Goodbye!!! See you next time.")