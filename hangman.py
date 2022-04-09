import random
from words import words
import string


def get_word(words):
    guess_word = random.choice(words)
    return guess_word.upper()


def name_game():
    secrete = get_word(words)
    secrete_letters = set(secrete)
    alphabet = set(string.ascii_uppercase)
    typed_letters = set()
    lives = (len(secrete_letters) * 2)

    print("NAME OF ANIMAL")
    print("")
    print("You have", lives, "tries")

    while len(secrete_letters) > 0 and lives != 0:

        print("")
        wordlist = [letter if letter in typed_letters else "_" for letter in secrete]
        print("Your current word is: ", " ".join(wordlist))
        guess = input("Enter a letter: ").upper()

        if guess in alphabet - typed_letters:
            typed_letters.add(guess)
            if guess in secrete_letters:
                secrete_letters.remove(guess)
            else:
                print(guess, "is not in the word.")
                lives -= 1
                print("")
                if lives > 1:
                    print("You have", lives, "lives left")
                else:
                    print("You have", lives, "live left")
        elif guess in typed_letters:
            print("You have used this letter")
        else:
            print("Invalid Input")

        print("you have used letter: ", ",".join(typed_letters))

    if lives == 0:
        print("")
        print("You lost, the animal name is", secrete)
    else:
        print("")
        print("You WON!!!")
        print(f"You guessed the animal {secrete} correctly.")


name_game()
