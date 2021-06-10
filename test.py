#!/usr/bin/env python
from brain_games.cli import welcome_user
from random import randint


def num_odd(random_number, player_answer, counter, username):
    while counter < 3:
        if int(random_number) % 2 == 0:
            if player_answer == 'yes':
                print('Correct!')
                counter += 1
                if counter == 3:
                    print(f'Congratulations, {username}!')
            else:
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\n Let's try again, {username}!")


def num_notodd(random_number, player_answer, counter, username):
    while counter < 3:
        if int(random_number) % 2 != 0:
            if player_answer == 'no':
                print('Correct!')
                counter += 1
            if counter == 3:
                print(f'Congratulations, {username}!')
            else:
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\n Let's try again, {username}!")


def start_game(username):
    counter = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while counter < 3:
        random_number = randint(1, 100)
        print('Question: ' + str(random_number))
        player_answer = input('Your answer: ')
        num_odd(random_number, player_answer, counter, username)
        num_notodd(random_number, player_answer, counter, username)


def main():
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print('Hello ' + user_name + '!')
    start_game(user_name)


if __name__ == '__main__':
    main()
