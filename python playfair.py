def generate_key_matrix(key):
    # Remove duplicates and create the key string
    key = ''.join(sorted(set(key), key=key.index))
    key = key.replace('J', 'I')  # Merge 'J' with 'I'

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' is removed
    matrix = []
    used = set(key)

    # Fill the matrix with the key followed by the remaining letters of the alphabet
    for char in key:
        if char not in used:
            matrix.append(char)
            used.add(char)

    for char in alphabet:
        if char not in used:
            matrix.append(char)
            used.add(char)

    # Convert the list to a 5x5 matrix
    return [matrix[i * 5:(i + 1) * 5] for i in range(5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, letter in enumerate(row):
            if letter == char:
                return i, j
    return None

def playfair_encrypt(plaintext, key):
    # Generate the key matrix
    matrix = generate_key_matrix(key)
    
    # Prepare the plaintext
    plaintext = plaintext.upper().replace('J', 'I')
    plaintext_pairs = []
    i = 0
    while i < len(plaintext):
        if i == len(plaintext) - 1:
            plaintext_pairs.append((plaintext[i], 'X'))
            i += 1
        elif plaintext[i] == plaintext[i + 1]:
            plaintext_pairs.append((plaintext[i], 'X'))
            i += 1
        else:
            plaintext_pairs.append((plaintext[i], plaintext[i + 1]))
            i += 2

    # Encrypt the plaintext pairs
    ciphertext = ''
    for pair in plaintext_pairs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext

def playfair_decrypt(ciphertext, key):
    # Generate the key matrix
    matrix = generate_key_matrix(key)
    
    # Prepare the ciphertext pairs
    ciphertext = ciphertext.upper().replace('J', 'I')
    ciphertext_pairs = [(ciphertext[i], ciphertext[i + 1]) for i in range(0, len(ciphertext), 2)]

    # Decrypt the ciphertext pairs
    plaintext = ''
    for pair in ciphertext_pairs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])

        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

    # Remove 'X' used as padding
    plaintext = plaintext.replace('X', '')
    return plaintext

# Example usage
key = "PLAYFAIRCIPHER"
plaintext = "HIDE THE GOLD IN THE TREE STUMP"

ciphertext = playfair_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")

decrypted_text = playfair_decrypt(ciphertext, key)
print(f"Decrypted Text: {decrypted_text}")
