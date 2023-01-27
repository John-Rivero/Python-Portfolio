#Tip Calculator
print ("Welcome to the tip calculator.")
totalBill = input("What was the total bill? ")

totalBill = float(totalBill)

totalTip = int (input("What percentage tip would you like to give? 10, 12, or 15? "))
peopleSplit = int (input("How many people to split the bill? "))

#conditional for the tip selection
if totalTip == 15:
    totalAmount = (totalBill / peopleSplit) * 1.15
    totalAmount = (round(totalAmount, 2))
    print ("Each person should pay: ${}".format(totalAmount))

elif totalTip == 12:
    totalAmount = (totalBill / peopleSplit) * 1.12
    totalAmount = (round(totalAmount, 2))
    print ("Each person should pay: ${}".format(totalAmount))
    
elif totalTip == 10:
    totalAmount = (totalBill / peopleSplit) * 1.10
    totalAmount = (round(totalAmount, 2))
    print ("Each person should pay: ${}".format(totalAmount))   