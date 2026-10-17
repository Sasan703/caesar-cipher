alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:

        current_position = alphabet.index(letter)

        shifted_position = current_position + shift_amount

        cipher_text += alphabet[shifted_position]

    print(f"Here is the encoded result: {cipher_text}")

        #alphabet.index(letter)
        #alphabet.index(letter) + shift_amount
encrypt(text, shift)




# Encrypt the original text using the supplied shift amount.

# Shift each letter forwards and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# Run encryption with the message and shift entered by the user.

