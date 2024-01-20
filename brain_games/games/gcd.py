import random


def random_numbers():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    expression = f'{number1} {number2}'
    print(f'Question: {expression}')
    return number1, number2


def is_number():
    number1, number2 = random_numbers()
    if number1 >= number2:
        number = number2
    else:
        number = number1
    while number > 0:
        if number1 % number == 0 and number2 % number == 0:
            correct_answer = number
            break
        else:
            number = number - 1
    return correct_answer
