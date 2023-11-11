from main import encrypt_caesar, decrypt_caesar

# Example
text = input("Text: ")
shift = int(input("Shift: "))

encrypted_text = encrypt_caesar(text, shift)
print(f"Encoded text = {encrypted_text}")

decrypted_text = decrypt_caesar(encrypted_text, shift)
print(f"Decoded text = {decrypted_text}")
