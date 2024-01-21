import prompt


NUMBER_OF_ATTEMPTS = 3


def game(rule, question_and_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rule)
    n = 0
    while n < NUMBER_OF_ATTEMPTS:
        question, correct_answer = question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) == str(correct_answer):
            print('Correct!')
            n += 1
        elif str(user_answer) != str(correct_answer):
            print(
                f"'{user_answer}'is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            break
    if n == NUMBER_OF_ATTEMPTS:
        print(f'Congratulations, {name}!')
