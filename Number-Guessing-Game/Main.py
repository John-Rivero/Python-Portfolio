from Logo import logo
from easyMode import easyMode
from hardMode import hardMode
import random


while True:
    computerRandomNumber = random.randrange(1, 100)
    print (logo)
    #print(computerRandomNumber) 
    
    userDifficulty = input ("What difficulty would you like to try? \n(1) for easy mode or (2) for hard mode: ")

    if userDifficulty == "1":
        print("\nYou have chosen the easy mode. You currently have 10 guesses to get the right answer. \n")
        easyMode()
        
    elif userDifficulty == "2":
        print("You have chosen the hard mode. You currently have 5 guesses to get the answer right. \n")
        hardMode()
    
    playAgain = input ("\nWould you like to play again? (y) for YES and (n) for NO: ")

    if playAgain == 'y':
        continue
    
    else:
        break
print ("\nThank you for playing the 'Guess the Number'.")
exit()