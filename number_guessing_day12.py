import random

EASY_LEVEL_CHANCES = 10
HARD_LEVEL_CHANCES = 5


def set_difficulty():
    level = input("Choose a difficulty easy or hard: ")
    if level == 'easy':
        return EASY_LEVEL_CHANCES
    else:
        return HARD_LEVEL_CHANCES


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"you did it. you guessed the answer {answer}")


def game():
    print("welcome to number guessing game")
    print('think of a number between 1 to 100')
    answer = random.randint(1, 100)
    chances = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {chances} attempts to guess the answer")
        guess = int(input("make a guess: "))
        chances = check_answer(guess, answer, chances)
        if chances == 0:
            print("you run out of chances")
            return
        elif guess != answer:
            print("guess again")


game()
