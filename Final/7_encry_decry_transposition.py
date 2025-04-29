def encrypt(plaintext, key):
    # Create a grid of columns based on the key length
    num_cols = len(key)
    num_rows = len(plaintext) // num_cols + (1 if len(plaintext) % num_cols != 0 else 0)
    
    # Create a table of empty strings for the encryption
    grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    
    # Fill the grid with plaintext characters
    plaintext_index = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if plaintext_index < len(plaintext):
                grid[row][col] = plaintext[plaintext_index]
                plaintext_index += 1
    
    # Create the cipher text by reading columns based on the key order
    cipher_text = ''
    for col in sorted(range(num_cols), key=lambda x: key[x]):
        for row in range(num_rows):
            if grid[row][col] != '':
                cipher_text += grid[row][col]
    
    return cipher_text


def decrypt(ciphertext, key):
    # Create a grid for decryption
    num_cols = len(key)
    num_rows = len(ciphertext) // num_cols
    
    # Create a table of empty strings for the decryption
    grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    
    # Create the position order based on the key
    col_order = sorted(range(num_cols), key=lambda x: key[x])
    
    # Fill the grid with cipher text characters based on the key order
    cipher_text_index = 0
    for col in col_order:
        for row in range(num_rows):
            if cipher_text_index < len(ciphertext):
                grid[row][col] = ciphertext[cipher_text_index]
                cipher_text_index += 1
    
    # Read the grid row by row to reconstruct the plaintext
    plaintext = ''.join(''.join(grid[row]) for row in range(num_rows))
    
    return plaintext


def main():
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key (must be a string of digits): ")
    
    # Perform encryption
    encrypted_text = encrypt(plaintext, key)
    print(f"\nEncrypted text: {encrypted_text}")
    
    # Perform decryption
    decrypted_text = decrypt(encrypted_text, key)
    print(f"\nDecrypted text: {decrypted_text}")


if __name__ == "__main__":
    main()



# Enter the plaintext: HELLO WORLD
# Enter the key (must be a string of digits): 3124

# Encrypted text: EOL HLW O

# Decrypted text: HELLO WORLD
