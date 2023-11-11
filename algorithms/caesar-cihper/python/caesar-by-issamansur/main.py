# Main module with funcs for encrypt and decrypt by caesar cihper

def encrypt_caesar(text: str, shift: int):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = ''
            min_ord = ord('a') if char.islower() else ord('A')
            shifted_ord = (ord(char) - min_ord + shift) % 26 
            shifted_char = chr(shifted_ord + min_ord)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(encrypted_text, shift):
    return encrypt_caesar(encrypted_text, -shift)

