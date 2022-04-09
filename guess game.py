import random
import time


def guess_user():
    secrete_numb = random.randint(1, 50)
    guess = ""
    guesscount = 0
    guesslimit = 7
    out_of_guesses = False

    while guess != secrete_numb and not out_of_guesses:
        if guesscount < guesslimit:
            guess = int(input("enter a number: "))
            time.sleep(1)
            if guess > secrete_numb:
                print("guess too high")
            elif guess < secrete_numb:
                print("guess too low")
            else:
                break
            guesscount += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("you lose")
        print("the number is ", secrete_numb)
    else:
        print("you guessed ", secrete_numb, " correctly")


guess_user()
