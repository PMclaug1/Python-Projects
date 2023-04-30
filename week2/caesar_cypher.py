import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    crypto_text = ""
    for i in text:
        if i in alphabet:
            if direction == "encode":
                new_letter = alphabet.index(i) + shift
                if new_letter > 25:
                    new_letter = abs(26 - new_letter)
                    crypto_text += alphabet[new_letter]
                else:
                    crypto_text += alphabet[new_letter]
            elif direction == "decode":
                new_letter = alphabet.index(i) - shift
                if new_letter < 0:
                    new_letter = 26 + new_letter
                    crypto_text += alphabet[new_letter]
                else:
                    crypto_text += alphabet[new_letter]
        else:
            crypto_text += i
    print(f"The decoded text is {crypto_text}")


print(art.logo)
end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text, shift, direction)
    restart = input("Do you want to restart? Type yes or no.\n").lower()
    if restart == "no":
        end = True
        print("Adios")

    
