from Game_data import data
from Logo import logo
import random


print(logo)

def celebrity1():
    celebrity = random.choice(data)
    return celebrity
    
    
def celebrity2():
    celebrity = random.choice(data)
    return celebrity

def compare(celeb1, celeb2):
    count1 = celeb1['follower_count']
    count2 = celeb2['follower_count']
    
    if count1 > count2:
        return celeb1['name']
        
    elif count2 > count1:
        return celeb2['name']

    
score = 0
while True:
    print (f'\nYour Current Score: {score}')
    person1 = celebrity1()
    person2 = celebrity2()

    name1 = person1['name']
    name2 = person2['name']

    userInput = int(input(f'Who has a higher follower count? press(1) for {name1}  or press(2) for {name2}: \n'))

    print(f'You selected {userInput}\n')

    print(f'{name1} has', person1['follower_count'])
    print(f'{name2} has', person2['follower_count'])

    actualResult = compare(person1, person2)


    if userInput == 1:
        if person1['follower_count'] > person2['follower_count']:
            score += 1
            print("\nYou are correct")
            
        elif person2['follower_count'] > person1['follower_count']:
            score -= 1
            print("\nYou are wrong")
        
        
    if userInput == 2:
        if person2['follower_count'] > person1['follower_count']:
            score += 1
            print("\nYou are correct")
            
        elif person1['follower_count'] > person2['follower_count']:
            score -= 1
            print("\nYou are wrong")
        

    playAgain = int(input("Would you like to play again? press(1) for YES or press(2) for NO\n" ))
    if playAgain == 1:
        continue
    
    elif playAgain == 2:
        break

print(f'\nYour total score is {score}')
print("Thank you for playing.")

