def create_matrix(text, key_length):
    """Create a matrix from the text with the given key length (number of columns)."""
    matrix = [text[i:i + key_length] for i in range(0, len(text), key_length)]
    if len(matrix[-1]) < key_length:
        matrix[-1] += ' ' * (key_length - len(matrix[-1]))  # Padding if last row is short
    return matrix

def row_column_encrypt(plaintext, key):
    """Encrypt the plaintext using the Row-Column Transposition Cipher."""
    key_length = len(key)
    matrix = create_matrix(plaintext, key_length)
    key_indices = sorted(range(len(key)), key=lambda k: key[k])

    ciphertext = ''
    for col in key_indices:
        for row in matrix:
            ciphertext += row[col]
    return ciphertext

def row_column_decrypt(ciphertext, key):
    """Decrypt the ciphertext using the Row-Column Transposition Cipher."""
    key_length = len(key)
    num_rows = len(ciphertext) // key_length
    matrix = [''] * num_rows
    key_indices = sorted(range(len(key)), key=lambda k: key[k])

    index = 0
    for col in key_indices:
        for row in range(num_rows):
            matrix[row] += ciphertext[index]
            index += 1

    plaintext = ''.join(matrix).rstrip()
    return plaintext

# Example usage
plaintext = "Attack at dawn"
key = "4312567"

ciphertext = row_column_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")

decrypted_message = row_column_decrypt(ciphertext, key)
print(f"Decrypted Message: {decrypted_message}")
