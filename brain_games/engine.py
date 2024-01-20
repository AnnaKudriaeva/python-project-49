import prompt


NUMBER_OF_ATTEMPTS = 3

def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def rule():
    print('What is the result of the expression?')


def your_answer():
    answer = prompt.string('Your answer: ')
    return answer


def game(is_number):
    name = welcome_user()
    rule()
    n = 0
    while n < NUMBER_OF_ATTEMPTS:
        correct_answer = is_number()
        ans = your_answer()
        if str(ans) == str(correct_answer):
            print('Correct!')
            n += 1
        elif str(ans) != str(correct_answer):
            print(
                f"'{ans}'is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            break
    if n == NUMBER_OF_ATTEMPTS:
        print(f'Congratulations, {name}!')