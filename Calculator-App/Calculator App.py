from Logo import logo


#Order of operation
def addition (n1, n2):
    return n1 + n2

def subtraction (n1, n2):
    return n1 - n2

def multiplication (n1, n2):
    return n1 * n2

def division (n1, n2):
    return n1 / n2

order_of_operation = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}

while True:
    print(logo)
    num1 = float(input("What is the first number?: "))
    num2 = float(input("What is the second number?: "))

    for key in order_of_operation:
        print(key)
        
    userOperation = input ("Which operation would you like to perform?: ")


    selectedOperation = order_of_operation[userOperation]
    total = selectedOperation(num1, num2)
    print(f'{num1} {userOperation} {num2} = {total}')
    
    continueQuestion = input("press (1) to continue or press (2) to quit")
    if continueQuestion == 1:
        continue
    elif continueQuestion == 2:
        break
    
print ("Thank you for using the calculator")