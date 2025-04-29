# Python program to AND and XOR each character in "Hello World" with 127

# Original string
text = "Hello World"

print("Original String:", text)
print("\nCharacter\tAND with 127\tXOR with 127")
print("-" * 40)

# Iterate through each character in the string
for char in text:
    # Apply AND operation with 127
    and_result = ord(char) & 127
    # Apply XOR operation with 127
    xor_result = ord(char) ^ 127
    # Print the character along with the results of AND and XOR operations
    print(f"{char}\t\t{and_result}\t\t{xor_result}")



# Original String: Hello World

# Character   AND with 127   XOR with 127
# ----------------------------------------
# H           72              55
# e           101             24
# l           108             19
# l           108             19
# o           111             16
#             32              95
# W           87              40
# o           111             16
# r           114             13
# l           108             19
# d           100             27
