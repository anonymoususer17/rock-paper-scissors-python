# Implementing a rock, paper scissors game, with optional lizard and spock
# I'm going with a simple CLI implementation first to get the (simple) logic down

# importing random for the machine choice
import random

# Choose a random number between 1 and 3
machineChoice = random.choice(range(3))

choices = ["Rock", "Paper", "Scissors"]
defaultPrompt = "Input the corresponding number for:\n0. Exit\n1. Rock\n2. Paper\n3. Scissors\n"

def startGame():
    playerChoice = int(input(defaultPrompt))
    wins = 0
    losses = 0
    
    while playerChoice != 0:
        machineChoice = random.choice(range(3))
        if playerChoice not in (1, 2, 3):
            playerChoice = int(input(f"Try again.\n{defaultPrompt}"))
        else:
            print("Machine choice: " + choices[machineChoice])
            match playerChoice - 1 - machineChoice:
                case 1 | -2:
                    print(choices[playerChoice - 1] + " beats " + choices[machineChoice] + ". You win!")
                    wins+=1
                case 0:
                    print("It's a tie")
                case _:
                    print(choices[machineChoice] + " beats " + choices[playerChoice - 1] + ". You lose...")
                    losses+=1
            playerChoice = int(input(f"Wins: {wins}, Losses: {losses}. Another round?"))

startGame()
