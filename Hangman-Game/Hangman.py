from hangman_art import stages
from hangman_art import logo
from random_word import RandomWords

randomWord = RandomWords()

print(logo)

#Randomly choose a word
randomWord = randomWord.get_random_word()
print(randomWord)

#create a list or blanks
blankList = []
blank = "_"
for wordCount in range(len(randomWord)):
  blankList.append(blank)
print(blankList, "\n")



endGame = False

counter = 0
while not endGame:
  guess = input("Enter the letter for your guess: ").lower()
  
  if guess in blankList:
      print("You have entered this letter. \n")
  
  #if the guess is wrong, hangman's life -1
  if guess not in randomWord:
    print(stages[counter])
    counter += 1
    if stages[counter] == stages[6]:
      print("You lost, Game Over")
      break

  for position in range (len(randomWord)):
    letter = randomWord[position]
    
    if letter == guess:
      blankList[position] = guess
  print(blankList, "\n")
      

  if blank not in blankList:
    print("You won")
    break