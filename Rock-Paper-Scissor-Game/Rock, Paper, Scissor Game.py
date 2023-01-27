import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


userInput = int(input("Choose (1) Rock, (2) Paper, (3) Scissor (4) to Quit: "))
computerGenerated = random.randint(1, 3)

while (userInput != 4):
    
    if (computerGenerated == 1):
        print ("The computer chose Rock ", rock)
        if (userInput == 1):
            print ("You have chosen Rock,", rock)
            print ("It is a tie")
        elif (userInput == 2):
            print ("You have chosen Paper", paper)
            print ("You won")
        elif (userInput == 3):
            print ("You have chosen Scissor", scissors)
            print ("You Lost")
        
    elif (computerGenerated == 2):
        print ("The computer chose Paper ",paper)
        if (userInput == 1):
            print ("You have chosen Rock,", rock)
            print ("You Lost")
        elif (userInput == 2):
            print ("You have chosen Paper", paper)
            print ("It is a tie")
        elif (userInput == 3):
            print ("You have chosen Scissor", scissors)
            print ("You won")
        
    elif (computerGenerated == 3):
        print ("The computer chose Scissor ",scissors)
        if (userInput == 1):
            print ("You have chosen Rock,", rock)
            print ("You won")
        elif (userInput == 2):
            print ("You have chosen Paper", paper)
            print ("You Lost")
        elif (userInput == 3):
            print ("You have chosen Scissor", scissors)
            print ("It is a tie")
    userInput = int(input("Choose (1) Rock, (2) Paper, (3) Scissor (4) to Quit: "))
    computerGenerated = random.randint(1, 3)