import string

alphabet = string.ascii_letters.lower()

print("Welcome to Caeser cipher!")
direction = input("Type 'encode' to encrypt, type 'decore' to decrypt:\n")
text = input("Type your message:\n").lower()
Shift = int(input("Type the shift number:\n"))

def caeser(code, message, key):
    cipher_text = ''
    for letter in text: 
        position = alphabet.index(letter)
        if direction == 'encode':
            new_position = (position + key) % 26
            cipher_text += alphabet[new_position]
        elif direction == 'decode':
            new_position = (position - key) % 26
            cipher_text += alphabet[new_position]
        else:
            print("You did not made a valid choise.")
    print(f"The {code}d text is {cipher_text}")

caeser(code= direction, message=text, key=Shift)


"""
#First version (with two functions)
def encrypt(message, key):
    cipher_text = ''
    for letter in text: 
        position = alphabet.index(letter)
        new_position = (position + key) % 26
        cipher_text += alphabet[new_position]
    return cipher_text

def decrypt(message, key):
    plain_text = ''
    for letter in text: 
        position = alphabet.index(letter)
        new_position = (position - key) % 26
        new_char = alphabet[new_position]
        plain_text += new_char
    return plain_text

decrypt(message= text, key= Shift)

if direction == 'encode':
    print(f"The encoded text is {encrypt(message= text, key= Shift)}")
elif direction == 'decode':
    print(f"The decoded text is {decrypt(message= text, key= Shift)}")
else:
    print("You did not made a valid choise.")
"""

