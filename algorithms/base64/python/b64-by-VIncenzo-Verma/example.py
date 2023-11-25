from main  import encrypt_64, decrypt_64
text = input('Enter message : ')
if(len(text) % 4 == 0 ):
    encoded = encrypt_64(text)
    print("Encrypted text : {}".format(encoded))
    print("Decrypted text : {}".format(decrypt_64(encoded)))
else:
    print("Length of input text must be a multiple of 4")
    
