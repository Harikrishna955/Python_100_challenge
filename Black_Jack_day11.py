import os
import random


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw-_-"
    elif computer_score == 0:
        return "you Lose. opponent has blackJack <___>"
    elif user_score == 0:
        return "win with a blackJack"
    elif user_score > 21:
        return "you went over.you lose"
    elif computer_score > 21:
        return "opponent went over. you win"
    elif user_score > computer_score:
        return 'You win'
    else:
        return 'you lose'


def play_game():
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f'your cards : {user_cards} and score : {user_score}')
        print(f'computer first card : {computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_chance = input('Type "y" to get another card, type "n" to pass: ').lower()
            if user_chance == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(compare(user_score, computer_score))

    print(f"your final hand: {user_cards}.final score : {user_score}")
    print(f"computer final hand: {computer_cards}.final score: {computer_score}")


play_game()

while input("type 'y' to play blackjack game again or type any 'key' to exit: ").lower() == 'y':
    os.system('cls')
    play_game()
