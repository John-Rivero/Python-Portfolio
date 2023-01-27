def compareTotals(user, computer):
    print(f"User's score: {user} | Computer's score: {computer}")
    if user > 21:
        print("You BUSTED, You LOST!!!")
        
    elif computer > 21:
        print("The computer BUSTED, You WON!!!")
        
    elif user > computer:
        print (f'You WON!!!!')
        
    else:
        print(f"You LOST!!! The computer won")