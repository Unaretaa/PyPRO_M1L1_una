import random
import time

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

pasword_lenght = int(input("Panjang password: "))

password = ""

for i in range(pasword_lenght):
    password += random.choice(characters)

print("Menyiapkan password anda...")
time.sleep(3)
print("Password anda : " + password)