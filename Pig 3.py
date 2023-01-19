import random
# user = input("Would you like to play? ")
# if user == "yes"

def roll_dice():

    roll = random.randint(1,6)

    return roll

user_score = 0
computer_score = 0

def user_turn(user_score, computer_score):
    total = 0
    user = "r"
    print("Total so far: ", total)
    user = input("Type r to roll again, or type h to hold. ")

    while user == "r":
        user_roll = roll_dice()


        if user_roll == 1:
            total = 0
            break

        else:
            total = user_roll + total


            print("Total so far: ", total)
            user = input("Type r to roll again, or type h to hold.")
        if user == "h":
            user_score = total + user_roll
            break
    return user_score


def computer_turn(user_score, computer_score):
    total2 = 0

    while True:
        computer_roll = roll_dice()
        if computer_roll == 1:
            computer_score = computer_score + 0
            break
        computer_score = total2 + computer_roll

        if total2 >= 20:
            computer_score = computer_score + total2
            break

    return computer_score


def check_score(user_score, computer_score):

    if user_score > computer_score and user_score > 100:
        print("You are the winner!")
    if user_score < computer_score and computer_score > 100:
        print("You have lost.")

def print_score(user_score, computer_score):
    score = user_turn(user_score, computer_score)
    score2 = computer_turn(user_score, computer_score)
    print("{:<5} is your score.".format(score))
    print("{:<5} is the computer's score.".format(score2))


while user_score < 100 and computer_score < 100:
    user_turn(user_score, computer_score)

    computer_turn(user_score, computer_score)
    print_score(user_score, computer_score)
    check_score(user_score, computer_score)
