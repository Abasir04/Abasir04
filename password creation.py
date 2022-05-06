import random
import string


def generator(length, amount):
    if length < 4:
        print("Caution! The length entered is too short")
        answer = input("Do you want to continue anyway, 'y' for yes any other key to exit: ")
        if answer == 'y':
            pass
        else:
            exit()

    keys = string.ascii_letters + string.digits + string.punctuation
    passwords = []

    for i in range(amount):
        password = ''
        for j in range(length):
            password += random.choice(keys)

        passwords.append(password)
        print(password)

    ans = input("Do you want to save your password, 'y' for yes any other key to exit: ")
    name = input("Enter the name of the file to save your password: ")
    if ans == 'y':
        with open(name + '.txt', 'a') as f:
            file = '\n'.join(passwords)
            f.write(file)
    else:
        exit()


x = int(input("Enter length of password: "))
y = int(input("Enter the amount of password: "))
generator(x, y)
