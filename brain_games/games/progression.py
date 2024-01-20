import random


def rule():
    print('What number is missing in the progression?')


def is_number():
    start_value = random.randint(1, 10)
    difference = random.randint(1, 5)
    num_elements = 10
    progression = [start_value + i * difference for i in range(num_elements)]
    index_to_replace = random.randint(0, len(progression) - 1)
    replaced_number = progression[index_to_replace]
    progression[index_to_replace] = '..'
    progression = ' '.join(map(str, progression))
    print(f'Question: {progression}')
    return replaced_number
