import prompt
from brain_games.template import is_greeting
from brain_games.template import CORRECT_ANSWER, ANSWER, QUESTION, NUMBER
from random import randint


DESC = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even():
    name =  is_greeting()
    print(DESC)
    print(f'{QUESTION}{NUMBER}')
    answer_input = prompt.string(ANSWER)
    return answer_input



