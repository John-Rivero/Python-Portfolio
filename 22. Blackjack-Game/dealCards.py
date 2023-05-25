import random

#Function that uses the List below to *return* a random card.
def dealCards (cardList):
    result = random.choice(cardList)
    return result