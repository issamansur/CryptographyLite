def xor_cipher(text, key):
    if key.isdigit():
        return ''.join([chr(ord(t) ^ int(key)) for t in text])
    else:
        return ''.join([chr(ord(t) ^ ord(k)) for t, k in zip(text, key * len(text))])