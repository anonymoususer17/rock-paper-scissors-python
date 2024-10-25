# Importing random for the machine choice
import random

class RPSGame:

    def startGame(chosen):
        playerChoice = chosen
        wins = 0
        losses = 0
        # Initializing default values
        choices = ["Rock", "Paper", "Scissors"]
        
        while playerChoice != 0:
            # Choose a random number between 1 and 3
            machineChoice = random.choice(range(3))
            print("Machine choice: " + choices[machineChoice])
            match playerChoice - 1 - machineChoice:
                case 1 | -2:
                    wins+=1
                    return (choices[playerChoice - 1] + " beats " + choices[machineChoice] + ". You win!")
                case 0:
                    return ("It's a tie")
                case _:
                    losses+=1
                    return (choices[machineChoice] + " beats " + choices[playerChoice - 1] + ". You lose...")
