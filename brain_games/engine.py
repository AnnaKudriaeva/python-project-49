from brain_games.cli import welcome_user
import prompt


NUMBER_OF_ATTEMPTS = 3


def greet():
    print('Welcome to the Brain Games!')


def your_answer():
    answer = prompt.string('Your answer: ')
    return answer


def game(rule, is_number):
    greet()
    name = welcome_user()
    rule()
    n = 0
    while n < NUMBER_OF_ATTEMPTS:
        correct_answer = is_number()
        answer = your_answer()
        if str(answer) == str(correct_answer):
            print('Correct!')
            n += 1
        elif str(answer) != str(correct_answer):
            print(
                f"'{answer}'is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            break
    if n == NUMBER_OF_ATTEMPTS:
        print(f'Congratulations, {name}!')
