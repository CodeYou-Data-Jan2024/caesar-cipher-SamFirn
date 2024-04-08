
def Caesar_Cipher():
    message = str(input("Hello, my names Caesar. What would you like to encrypt today?\n :"))
    shift = int(input("Amount to shift? (example:5)\n :"))
    caesar = ""

    for char in message:
        if char.isalpha():
            key = ord(char)
            lock = key + shift
            cipher = chr(lock)
            caesar += cipher
        elif char.isnumeric():
            key = ord(char)
            lock = key + shift
            cipher = chr(lock)
            caesar += cipher
        else:
            caesar += char
            
    print(caesar)

Caesar_Cipher()