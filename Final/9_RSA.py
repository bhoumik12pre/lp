import random

def gcd(a, b):
    """Compute the Greatest Common Divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """Compute the modular inverse of e modulo phi using Extended Euclidean Algorithm."""
    d_old, d_new = 0, 1
    r_old, r_new = phi, e
    while r_new != 0:
        quotient = r_old // r_new
        d_old, d_new = d_new, d_old - quotient * d_new
        r_old, r_new = r_new, r_old - quotient * r_new
    if r_old > 1:
        return None  # No modular inverse if e and phi are not coprime
    return d_old % phi

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generate_keypair(p, q):
    """Generate RSA key pair (public and private keys)."""
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')  # Ensure p and q are prime
    elif p == q:
        raise ValueError('p and q cannot be the same.')  # Ensure p and q are not the same

    n = p * q  # Modulus for both public and private keys
    phi = (p-1) * (q-1)  # Euler's totient function

    # Choose e such that e and phi(n) are coprime
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Compute d (modular inverse of e)
    d = mod_inverse(e, phi)

    # Public key (e, n), Private key (d, n)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    """Encrypt plaintext using a public key."""
    key, n = pk
    # Convert each letter into numbers based on character code and encrypt using public key
    cipher = [(pow(ord(char), key, n)) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    """Decrypt ciphertext using a private key."""
    key, n = pk
    # Decrypt ciphertext using private key and convert back to characters
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

# Driver code
if __name__ == "__main__":
    print("RSA Encryption/Decryption")
    p = int(input("Enter a prime number (p): "))  # Get prime number p
    q = int(input("Enter another prime number (q): "))  # Get prime number q

    public, private = generate_keypair(p, q)  # Generate public and private keys
    print("\nPublic key:", public)  # Display public key
    print("Private key:", private)  # Display private key

    message = input("\nEnter a message to encrypt: ")  # Get message to encrypt
    encrypted_msg = encrypt(public, message)  # Encrypt the message with public key
    print("\nEncrypted message:", encrypted_msg)  # Display encrypted message

    decrypted_msg = decrypt(private, encrypted_msg)  # Decrypt the message with private key
    print("Decrypted message:", decrypted_msg)  # Display decrypted message



# RSA Encryption/Decryption
# Enter a prime number (p): 61
# Enter another prime number (q): 53

# Public key: (103, 3233)
# Private key: (939, 3233)

# Enter a message to encrypt: Hello

# Encrypted message: [1771, 1675, 2999, 2999, 2641]

# Decrypted message: Hello
