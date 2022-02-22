import random # To generate random ASCII 
import string # To generate ASCII 

""" GLOBAL VARIABLE """
LETTERS = string.ascii_letters
SYMBOLS = string.punctuation
DIGITS = string.digits


def generateUsername():
    generate_username = random.choices(LETTERS + DIGITS, k=8) # Generate random string for making one username 

    userName = "".join(generate_username)

    return userName

def generatePassword():
    generate_password = random.choices(LETTERS + DIGITS + SYMBOLS, k = 24)

    passWord = "".join(generate_password)

    return passWord

def fileHandler():
    userName = generateUsername()
    passWord = generatePassword()
    files = open("passwd.txt", "a")
    files.write(userName + "\n")
    files.write(passWord + "\n")

def validation():
    userName = generateUsername()
    passWord = generatePassword()
    # Opening File 
    files = open("passwd.txt", "r")

    for username in files:
        if username == userName:
            return "Not Valid, There's a same username inside list"
        else:
            return "Success!"

    for password in files:
        if password == passWord:
            return "Not Valid, There's a same password inside list"
        else:
            return "Success!"

if __name__ == '__main__':
    fileHandler()
    validation()
