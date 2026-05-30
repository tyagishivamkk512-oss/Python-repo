import random
import string

char = string.ascii_letters + string.digits + string.punctuation + " "
char = list(char)
key = char.copy()
random.shuffle(key)

#ENCRYPTION

text = input("enter your message: ")
encrypted = ""

for letter in text:
    index = char.index(letter)
    encrypted += key[index]

print(f"your encrypted message: {encrypted}")

#DECRYPTION

text2 = input("enter your message: ")
decrypted = ""

for letter in text2:
    index = key.index(letter)
    decrypted += char[index]

print(f"your decrypted message: {decrypted}")