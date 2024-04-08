def caesar_bot():
    message = str(input("Hello, my names Caesar. Please enter a message you would you like to encrypt today:\n"))
    shift = int(input("Amount to shift? (example:5):\n"))
    caesar = ""
    classic_key_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    classic_key_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for char in message:
        if char.isalpha():# for the characters in the message that are letters
            if char.isupper(): # for Uppercase Letters
                key = classic_key_upper.index(char) #getting index position for character in message
                lock = key + shift # adding the shift to value
                if lock > 25: # to prevent value exceeding max given index position
                    lock -= 26
                cipher = classic_key_upper[lock]#becomes character at the shifted index position
                caesar += cipher # adds coded character to new message
            if char.islower(): # all the same but for lowercase letters
                key= classic_key_lower.index(char)
                lock = key + shift
                if lock > 25:
                    lock -= 26
                cipher = classic_key_lower[lock]
                caesar += cipher
        elif char.isdigit(): # for if character is a number
                coded_number = int(char) + shift #adding shift amount  to number in message
                caesar += str(coded_number) #adding new number to message
        else:
            caesar += char #adds spaces and punction to new message
    print(caesar)

caesar_bot()