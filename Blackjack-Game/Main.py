from Logo import logo
from dealCards import dealCards
from calculate_score import calculate_score
from hit_or_not import hit_or_not
from compareTotals import compareTotals

cards = [11,2,3,4,5,6,7,8,9,10]

while True:
    print (logo)
    #USER CARDS
    user = []
    for i in range (2):
        user.append(dealCards(cards))
    print (f"Your Card: {user}")

    userResult = calculate_score(user)
    print(f"The current value of your card is: {userResult}\n")

    #While loop for a hit or not
    while (userResult <= 21):
        userInputHitorNo = input("Would you like to hit or no? Press (y) for yes or (n) for no: ")
        
        if userInputHitorNo == "y":
            hitCard = hit_or_not(cards)
            print(f'The card that you received is: {hitCard}')
            
            #give the user an option to either keep 1 or 11 for 11
            if hitCard == 11:
                one_or_eleven = int(input("Would you like to keep your card as a 1 or 11?: "))
                if one_or_eleven == 11:
                    hitCard = 11
                    
                elif one_or_eleven == 1:
                    hitCard = 1
            
            userResult += hitCard
            
            print(f'The total value of your cards is: {userResult}\n')
            continue
    
        else:
            print(f'The total value of your cards is: {userResult}\n')
            break

    #COMPUTER'S CARDS
    computer = []
    for i in range (2):
        computer.append(dealCards(cards))

    computerResult = calculate_score(computer)
    while computerResult <= 17:
        hitCard = hit_or_not(cards)
        computerResult += hitCard

    compareTotals(userResult, computerResult)
    
    continue_or_not = input ("Would you like to play again? (y) for Yes or (n) for No: ")
    if continue_or_not == "y":
        continue
    else:
        print("Thank you for playing Blackjack. ")
        break