#  start coding for the caesar cipher encription
# define the encryption codes
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Only alphabetical characters  should be encrypted
            shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
            encrypted_text += shifted_char
        else:
            # Keep non-alphabetical characters unchanged
            encrypted_text += char
    return encrypted_text

# Collect entries from user input
plain_text = input("Enter the plain text sentence: ")

# Encrypt the text using Caesar cipher with a right shift of 5
encrypted_text = caesar_cipher_encrypt(plain_text, shift=5)

# Display the encrypted text
print("Encrypted Text:", encrypted_text)