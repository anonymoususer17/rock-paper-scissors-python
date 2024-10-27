# Importing random for the machine choice
import random

class RPSGame:

    def startGame(chosen, responseObj):
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
                    responseObj.wins+=1
                    responseObj.playerMessage = choices[playerChoice - 1] + " beats " + choices[machineChoice] + ". You win!"
                case 0:
                    responseObj.ties+=1
                    responseObj.playerMessage = ("It's a tie")
                case _:
                    responseObj.losses+=1
                    responseObj.playerMessage =  (choices[machineChoice] + " beats " + choices[playerChoice - 1] + ". You lose...")

            return responseObj;
