from main import xor_cipher

text = input("Enter a string: ")
key = input("Enter a key: ")

encrypted = xor_cipher(text, key)
decrypted = xor_cipher(encrypted, key)

print("Encrypted: " + encrypted)
print("Decrypted: " + decrypted)