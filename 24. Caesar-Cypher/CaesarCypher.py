from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(Usertext, Usershift, Userdirection):
    string = ""
    
    if Userdirection == "encode":
        for text2 in Usertext:
            position = alphabet.index(text2)
            newPosition = alphabet[position + Usershift]
            string += newPosition
        print(f"Your encoded word is {string}")

        
    elif Userdirection == "decode":
        for text2 in Usertext:
            position = alphabet.index(text2)
            newPosition = alphabet[position - Usershift]
            string += newPosition
        print(f"Your decoded word is {string}")
        


while True:
    print (logo)
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode":
        text = input("Type your message:\n").lower()
        for textTest in text:
            if textTest not in alphabet:
                print("ERROR, Unknown input (no symbol/number/space).")
                continue
                
            else:
                shift = int(input("Type the shift number:\n"))
                Updatedshift = shift % 26

                caesar(Usertext=text, Usershift=Updatedshift, Userdirection=direction)
                break
        
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        for textTest in text:
            if textTest not in alphabet:
                print("ERROR, Unknown input (no symbol/number/space).")
                continue
                
            else:
                shift = int(input("Type the shift number:\n"))
                Updatedshift = shift % 26

                caesar(Usertext=text, Usershift=Updatedshift, Userdirection=direction)
                break

    else:
        print ("ERROR, Unknown input, please try again. ")
        continue
    
    
    restartEndInput = input ("Would you like to restart or end? ")
    if restartEndInput == "restart":
        continue
    elif restartEndInput == "end":
        print("Thank you for using Caesar Cipher, goodbye.")
        break
    else:
        print("ERROR, Unknown input, please try again")
        continue