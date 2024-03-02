import secrets
import string

def createPw(pwLength=12):
    letters = string.ascii_letters
    digits = string.digits
    specialChars = string.punctuation

    alphabet = letters + digits + specialChars
    pwd = ''
    pwStrong = False

    while not pwStrong:
        pwd = ''
        for i in range(pwLength):
            pwd += ''.join(secrets.choice(alphabet))

        if (any(char in specialChars for char in pwd) and
            sum(char in digits for char in pwd) >= 2):
            pwStrong = True
    
    return pwd

if __name__ == '__main__':
    print(createPw())