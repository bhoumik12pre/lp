#DES
#pip install pycryptodome
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

# Function to pad the text to be a multiple of 8 bytes (DES block size)
def pad(text):
    # Pad the text to be a multiple of 8 bytes
    while len(text) % 8 != 0:
        text += ' '  # Add spaces to make the text length a multiple of 8
    return text

# Encrypt the text using DES
def encrypt(text, key):
    # Pad the text to be a multiple of 8 bytes
    text = pad(text)
    cipher = DES.new(key, DES.MODE_ECB)  # Create a DES cipher object in ECB mode
    encrypted_text = cipher.encrypt(text.encode('utf-8'))  # Encrypt the text
    return base64.b64encode(encrypted_text).decode('utf-8')  # Return the encrypted text as a base64 string

# Decrypt the text using DES
def decrypt(encrypted_text, key):
    encrypted_text = base64.b64decode(encrypted_text)  # Decode the base64 encrypted text
    cipher = DES.new(key, DES.MODE_ECB)  # Create a DES cipher object in ECB mode
    decrypted_text = cipher.decrypt(encrypted_text).decode('utf-8')  # Decrypt the text
    return decrypted_text.strip()  # Remove any padding from the decrypted text

# Main function to demonstrate encryption and decryption
def main():
    # 8-byte key for DES
    key = get_random_bytes(8)  # Generate a random 8-byte key for DES

    # Sample text to encrypt
    text = "Hello, this is a DES encryption example!"  # Sample plaintext

    # Encrypt the text
    encrypted_text = encrypt(text, key)  # Encrypt the sample text
    print(f"Encrypted Text: {encrypted_text}")  # Display the encrypted text

    # Decrypt the text
    decrypted_text = decrypt(encrypted_text, key)  # Decrypt the encrypted text
    print(f"Decrypted Text: {decrypted_text}")  # Display the decrypted text

if __name__ == "__main__":
    main()  # Run the main function to demonstrate encryption and decryption
