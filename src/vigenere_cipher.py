def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    key = key.upper()

    ciphertext = ""

    for i, char in enumerate(plaintext):
        if char.isalpha():
            # Convert letters to numbers (A=0, B=1, etc.)
            p = ord(char) - ord('A')
            k = ord(key[i % len(key)]) - ord('A')

            # Apply Vigenère formula: (p + k) mod 26
            c = (p + k) % 26

            # Convert back to letter
            ciphertext += chr(c + ord('A'))
        else:
            ciphertext += char

    return ciphertext


def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.replace(" ", "").upper()
    key = key.upper()

    plaintext = ""

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            # Convert letters to numbers (A=0, B=1, etc.)
            c = ord(char) - ord('A')
            k = ord(key[i % len(key)]) - ord('A')

            # Apply Vigenère decryption formula: (c - k) mod 26
            p = (c - k) % 26

            # Convert back to letter
            plaintext += chr(p + ord('A'))
        else:
            plaintext += char

    return plaintext


def main():
    message = "HelloWorld"
    key = "secretkeythatdoesnothavetohavethesamelength"

    # Encrypt the message
    encrypted = vigenere_encrypt(message, key)
    print(f"Original message: {message}")
    print(f"Key: {key}")
    print(f"Encrypted message: {encrypted}")

    # Decrypt the message
    decrypted = vigenere_decrypt(encrypted, key)
    print(f"Decrypted message: {decrypted}")


if __name__ == "__main__":
    main()