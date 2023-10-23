import string

# Define the alphabet
alphabet = string.ascii_lowercase

def encrypt(message, shift):
    encrypted_text = ""

    for char in message:
        if char in alphabet:
            char_index = alphabet.index(char)
            new_index = (char_index + shift) % 26
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(encrypted_message, shift):
    decrypted_text = ""

    for char in encrypted_message:
        if char in alphabet:
            char_index = alphabet.index(char)
            new_index = (char_index - shift) % 26
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += char

    return decrypted_text

if __name__ == "__main__":
    choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()

    if choice == 'E':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == 'D':
        encrypted_message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = decrypt(encrypted_message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Enter 'E' for encryption or 'D' for decryption.")
