import random


def is_number():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    expression = f'{number1} {number2}'
    if number1 >= number2:
        num = number2
    else:
        num = number1
    while num > 0:
        if number1 % num == 0 and number2 % num == 0:
            correct_answer = num
            break
        else:
            num = num - 1
    print(f'Question: {expression}')
    return correct_answer
