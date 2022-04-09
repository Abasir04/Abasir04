import random


def play():
    print("Welcome to RPS")
    up = 0
    cp = 0
    tie = 0
    while True:
        print("")
        user = input("choose rock, paper, scissors or q to quit: ")
        if user == "quit":
            print("You won", up, "games. I won", cp, "games. We drew", tie, "games.")
            if up > cp:
                print("YOU WON!!!")
            elif cp > up:
                print("YOU LOST!!!")
            else:
                print("WE TIED")
            quit()

        computer = random.choice(["rock", "paper", "scissors"])
        print("I choose", computer)
        if user == computer:
            print("It is draw")
            tie += 1

        if is_win(user, computer):
            print("you won")
            up += 1

        if is_win(computer, user):
            print("you lost")
            cp += 1

        continue


def is_win(p, o):
    if (p == "rock" and o == "scissors") or (p == "scissors" and o == "paper") or (p == "paper" and o == "rock"):
        return True


play()
