def generate_key(message, key):
    """Generate a key that is the same length as the message."""
    key = list(key)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(message, key):
    """Encrypt the message using the Vigenère cipher."""
    encrypted_message = []
    key = generate_key(message, key)
    for i in range(len(message)):
        if message[i].isalpha():
            shift = (ord(message[i].upper()) + ord(key[i].upper())) % 26
            encrypted_char = chr(shift + ord('A'))
            if message[i].islower():
                encrypted_message.append(encrypted_char.lower())
            else:
                encrypted_message.append(encrypted_char)
        else:
            encrypted_message.append(message[i])  # Non-alphabetic characters are not encrypted
    return "".join(encrypted_message)

def vigenere_decrypt(ciphertext, key):
    """Decrypt the ciphertext using the Vigenère cipher."""
    decrypted_message = []
    key = generate_key(ciphertext, key)
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = (ord(ciphertext[i].upper()) - ord(key[i].upper()) + 26) % 26
            decrypted_char = chr(shift + ord('A'))
            if ciphertext[i].islower():
                decrypted_message.append(decrypted_char.lower())
            else:
                decrypted_message.append(decrypted_char)
        else:
            decrypted_message.append(ciphertext[i])  # Non-alphabetic characters are not decrypted
    return "".join(decrypted_message)

# Example usage
message = "Attack at dawn!"
key = "LEMON"

ciphertext = vigenere_encrypt(message, key)
print(f"Ciphertext: {ciphertext}")

decrypted_message = vigenere_decrypt(ciphertext, key)
print(f"Decrypted Message: {decrypted_message}")
