from random import randint, choice
from brain_games.cli import welcome_user


def start_game(username):
    counter = 0
    print('What number is missing in the progression?')
    while counter < 3:
        progression = randint(1, 100)
        number = randint(1, 50)
        length = 10
        max_number = (number * length) + progression
        question = range(progression, max_number, number)
        secrets = choice(question)
        riddle = ' '.join(['..' if num == secrets else str(num) for num in question])
        print(f'Question: {riddle}')
        player_answer = input('Your answer: ')
        if str(player_answer) == str(secrets):
            print('Correct!')
            counter += 1
            if counter == 3:
                print(f'Congratulations, {username}!')
        else:
            print(
                f"Your answer: {player_answer}\n{player_answer} is wrong answer ;(. Correct answer was {secrets}.\nLet's try again, {username}!")


def main():
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print('Hello ' + user_name + '!')
    start_game(user_name)


if __name__ == '__main__':
    main()
