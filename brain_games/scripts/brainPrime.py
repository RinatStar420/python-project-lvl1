"""
Игра "Простое ли число?"

Пример:

$ brain-prime

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Answer "yes" if given number is prime. Otherwise answer "no".
Question: 7
Your answer: yes
Correct!
"""
from random import randint

from brain_games.cli import welcome_user


def start_game(username):
    counter = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    while counter < 3:
        question_numb = randint(0, 100)
        print('Question: ' + str(question_numb))
        player_answer = input('Your answer: ')
        if int(question_numb) % 2 != 0:
            if player_answer == 'yes':
                print('Correct!')
                counter += 1
            else:
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\n Let's try again, {username}!")
        if int(question_numb) % 2 == 0:
            if player_answer == 'no':
                print('Correct!')
                counter += 1
            else:
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\n Let's try again, {username}!")
        if int(question_numb) == 2:
            if player_answer == 'yes':
                print('Correct!')
                counter += 1
            else:
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\n Let's try again, {username}!")
    if counter == 3:
        print(f'Congratulations, {username}!')


def main():
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print('Hello ' + user_name + '!')
    start_game(user_name)


if __name__ == '__main__':
    main()
