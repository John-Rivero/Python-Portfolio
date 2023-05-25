from Logo import logo
import os

print(logo)
emptyDict = {}



while True:
    
    userNameInput = input ("What is your name? \n")
    print(f'You entered {userNameInput}.')
    
    bidPriceInput = input ("What is your bid price? \n")
    print (f'You entered ${bidPriceInput}. ')
    
    emptyDict[userNameInput] = bidPriceInput
    
    userQuestion = input ("Are there anymore bidder? (Y for yes and N for No) \n")
    
    if userQuestion == "Y":
        os.system('cls')
        continue
    
    elif userQuestion == "N":
        break
    

highestBidValue = max(emptyDict.values())
highestBidKey = max(emptyDict, key=emptyDict.get)
print(f'The highest bid goes to {highestBidKey} with a bid of ${highestBidValue}.')