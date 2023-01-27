from Logo import logo
from Logo import logo2
from Menu import menu
from Resources import resources

def payment():
    quarterAmount = int(input ("How many quarters ($0.25) would you like to pay? "))
    quarter = quarterAmount * 0.25
    
    dimesAmount = int(input ("How many dimes ($0.10) would you like to pay? "))
    dimes = dimesAmount * 0.10
        
    nicklesAmount = int(input ("How many nickles ($0.05) would you like to pay? "))
    nickles = nicklesAmount * 0.05
    
    penniesAmount = int(input ("How many nickle ($0.01) would you like to pay? "))
    pennies = penniesAmount * 0.01
    
    total = quarter + dimes + nickles + pennies
    return total

espressoPrice = menu['espresso']['cost']
lattePrice = menu['latte']['cost']
cappuccinoPrice = menu['cappuccino']['cost']

waterResources = resources['water']
milkResources = resources['milk']
coffeeResources = resources['coffee']

while True:
    waterResources
    milkResources
    coffeeResources
    
    def calculateWater (userInput, waterResources):
        if userInput == "E":
            waterResources -= (menu["espresso"]['ingredients']['water'])
        
        if userInput == "L":
            waterResources -= (menu["latte"]['ingredients']['water'])
    
        if userInput == "C":
            waterResources -= (menu["cappuccino"]['ingredients']['water'])
        
        return waterResources

    def calculateMilk (userInput, milkResources):
        if userInput == "E":
            milkResources -= (menu["espresso"]['ingredients']['milk'])
        
        if userInput == "L":
            milkResources -= (menu["latte"]['ingredients']['milk'])
    
        if userInput == "C":
            milkResources -= (menu["cappuccino"]['ingredients']['milk'])
        
        return milkResources

    def calculateCoffee (userInput,coffeeResources):
        if userInput == "E":
            coffeeResources -= (menu["espresso"]['ingredients']['coffee'])
            
        if userInput == "L":
            coffeeResources -= (menu["latte"]['ingredients']['coffee'])
        
        if userInput == "C":
            coffeeResources -= (menu["cappuccino"]['ingredients']['coffee'])
            
        return coffeeResources
    
    userInput = input (f'What would you like to drink? \nEspresso       price:${espressoPrice}     press(E)      \nLatte          price:${lattePrice}     press(L) \nCappuccino     price:${cappuccinoPrice}     press(C) \nReport                        press(R): \nANSWER: ')
    
    if userInput == "E":
        if espressoPrice == payment():
            print("\nHere is your order: ")
            print(logo2)
            waterResources = calculateWater(userInput, waterResources)
            milkResources = calculateMilk (userInput, milkResources)
            coffeeResources = calculateCoffee (userInput,coffeeResources)
                
        elif espressoPrice != payment():
            print("Unsufficient amount, refunding your money now\n")
                
    elif userInput == "L":
        if lattePrice == payment():
            print("\nHere is your order: ")
            print(logo2)
            waterResources = calculateWater(userInput, waterResources)
            milkResources = calculateMilk (userInput, milkResources)
            coffeeResources = calculateCoffee (userInput,coffeeResources)
                
        elif lattePrice != payment():
            print("Unsufficient amount, refunding your money now\n")
                
    elif userInput == "C":
        if cappuccinoPrice == payment():
            print("\nHere is your order: ")
            print(logo2)
            waterResources = calculateWater(userInput, waterResources)
            milkResources = calculateMilk (userInput, milkResources)
            coffeeResources = calculateCoffee (userInput,coffeeResources)
                
        elif cappuccinoPrice != payment():
            print("Unsufficient amount, refunding your money now\n")
            

    print(f'\nYour current report: \nWater: {waterResources} \n Milk: {milkResources} \nCoffee: {coffeeResources}\n')    
    if (waterResources < 100) or (milkResources < 80) or (coffeeResources < 50):
        print("\nIm sorry, this vending machine does not have enough resources to create any more drinks")
        break
    

    
        
    drinkAgain = int(input("To get more drinks press(1) to quit press(2): "))
    if drinkAgain == 1:
        continue
    
    else:
        break
    
print("\nThank you for using this veding machine")