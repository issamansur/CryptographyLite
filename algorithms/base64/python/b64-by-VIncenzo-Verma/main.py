import base64

def encrypt_64(text: str):
    return base64.b64decode(text)

def decrypt_64(text: str):
    return base64.b64encode(text)