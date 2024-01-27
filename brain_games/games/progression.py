import random


RULE = 'What number is missing in the progression?'


def get_question_and_answer():
    start_value = random.randint(1, 10)
    difference = random.randint(1, 5)
    num_elements = 10
    progression = [start_value + i * difference for i in range(num_elements)]
    index_to_replace = random.randint(0, len(progression) - 1)
    correct_answer = progression[index_to_replace]
    progression[index_to_replace] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
