alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text,shift_amt):
    encrypted_text = ""
    for i in plain_text:
        new_letter = alphabet.index(i) + shift_amt
        if new_letter > 25:
            new_letter = abs(26 - new_letter)
        encrypted_text += alphabet[new_letter]
    print(f"The encoded text is {encrypted_text}")

def decrypt(encrypted_text, shift_amt):
    decrypted_text = ""
    for i in encrypted_text:
        new_letter = alphabet.index(i) - shift_amt
        if new_letter < 0:
            new_letter = 26 + new_letter
        decrypted_text += alphabet[new_letter]
    print(f"The encoded text is {decrypted_text}")

if direction == "encode":
    encrypt(plain_text = text,shift_amt = shift)
else:
    decrypt(encrypted_text = text,shift_amt = shift)



