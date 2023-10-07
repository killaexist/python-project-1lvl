import prompt
from random import randint, choice


CORRECT_ANSWER = 'Correct!'
ANSWER = 'Your answer: '
QUESTION = 'Question: '
NUMBER = randint(0, 99)


def is_greeting():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


