import random
import math
from brain_games.cli import welcome_user


def start_game(username):
    counter = 0
    print('Find the greatest common divisor of given numbers.')
    while counter < 3:
        first_numb = random.randint(0, 100)
        second_numb = random.randint(0, 100)
        answer = math.gcd(first_numb, second_numb)
        print('Question: ' + str(first_numb) + " " + str(second_numb))
        player_answer = input('Your answer: ')
        if str(player_answer) == str(answer):
            print('Correct!')
            counter += 1
            if counter == 3:
                print(f'Congratulations, {username}!')
        else:
            print(
                f"Your answer: {player_answer}\n{player_answer} is wrong answer ;(. Correct answer was {answer}.\nLet's try again, {username}!")


def main():
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print('Hello ' + user_name + '!')
    start_game(user_name)


if __name__ == '__main__':
    main()
