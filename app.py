# create a rock paper scissors game using python
# import random module
import random
# create a list of play options
t = ["rock", "paper", "scissors"]
score = 0
rounds = 0
# set player to False
player = False
while player == False:
# set player to True
    # assign a random play to the computer
    computer = t[random.randint(0, 2)]
    player = input("rock, paper, scissors? ")
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
            score += 1
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
            score += 1
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
            score += 1
    else:
        print("That's not a valid play. Check your spelling!")
    rounds += 1
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        player = True
        # print rounds played and score
        print("You played", rounds, "rounds")
        print("Your score is", score)
    else:
        player = False
    