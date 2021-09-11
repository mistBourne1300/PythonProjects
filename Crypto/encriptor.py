import os

def remove_spaces(plaintext):
    new_text = ''
    for c in plaintext:
        if c.isalpha():
            new_text += c
    return new_text

def encript(plaintext, encriptkey):
    plaintext = remove_spaces(plaintext)
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr(((ord(plaintext[i]) + encriptkey - 97) % 26) + 97)
    return ciphertext

#print("\n\n\n" + os.getcwd())
lotr_text = open("Desktop/Python/Crypto/lotr.txt", 'r+')
#print(lotr_text.closed)


plaintext = lotr_text.read()
plaintext = plaintext.lower()
print(remove_spaces(plaintext))
encription = encript(plaintext, 17)
print(encription)
encripted_text = open("Desktop/Python/Crypto/encripted.txt", 'r+')
encripted_text.write(encription)
print("check the encription file...")

