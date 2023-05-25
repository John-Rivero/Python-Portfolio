import random

computerRandomNumber = random.randrange(1, 100)


#This is the hard mode
#This also determines whether or not the guess is correct
def hardMode():
    currentNumberGuess = 5
    userGuess = int(input ("Please enter the number of your guess?: "))
    print (f'You entered {userGuess} \n')
    while currentNumberGuess >= 1:
        
        if currentNumberGuess == 1:
            print ("You have no more guesses left, GAME OVER!!!")
            break
        
        if userGuess == computerRandomNumber:
            print ("Congratulations!!! You have successfully guessed the right number")
            break
        
        elif userGuess != computerRandomNumber:
            if userGuess > computerRandomNumber:
                print ("Your guess is too high, Try again.")
                
            elif userGuess < computerRandomNumber:
                print ("Your guess is too low, Try again.")
            
        currentNumberGuess -= 1
        print (f"Your current number of guesses left: {currentNumberGuess}.\n")
        
        userGuess = int(input ("Please enter the number of your guess?: "))
        print (f'You entered {userGuess} \n')