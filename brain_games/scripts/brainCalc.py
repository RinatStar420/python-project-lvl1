import random
import prompt
from brain_games.cli import welcome_user


def start_game(username):
    counter = 0
    print('What is the result of the expression?')
    while counter < 3:
        first_numb = random.randint(0, 100)
        second_numb = random.randint(0, 100)
        numb_sum = first_numb + second_numb
        numb_diff = first_numb - second_numb
        numb_multi = first_numb * second_numb
        answer = random.choice([numb_sum, numb_diff, numb_multi])
        if answer == numb_sum:
            operation = '+'
        elif answer == numb_diff:
            operation = '-'
        else:
            operation = '*'
        print('Question:', first_numb, operation, second_numb)
        user_answer = prompt.string('Your answer: ')
        if str(answer) == user_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was {answer}.\nLet's try again, {username}!")
        if counter == 3:
            print(f'Congratulations, {username}!')


def main():
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print('Hello ' + user_name + '!')
    start_game(user_name)


if __name__ == '__main__':
    main()
