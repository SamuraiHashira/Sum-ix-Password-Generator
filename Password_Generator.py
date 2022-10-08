import string
import random

x1 = list(string.ascii_lowercase)
x2 = list(string.ascii_uppercase)
x3 = list(string.digits)
x4 = list(string.punctuation)

characters_number = input("How many characters in this Password?: ")

while True:
    try:
        characters_number = int(characters_number)
        if characters_number < 6 :
            print("you need at least 6 characters")
            characters_number = input("Please enter the number again: ")
        else:
            break
    except:
            print("Please enter numbers only")
            characters_number = input("How many characters in this Password?: ")

random.shuffle(x1)
random.shuffle(x4)
random.shuffle(x3)
random.shuffle(x2)


part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))
part3 = round(characters_number * (30/100))
part4 = round(characters_number * (20/100))

password = []
for i in range(part1):
    password.append(x1[i])
    password.append(x2[i])

for i in range(part2):
    password.append(x3[i])
    password.append(x4[i])

random.shuffle(password)
password = "".join(password[0:])


print("Your new password is: " +password)
