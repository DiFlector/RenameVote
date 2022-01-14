# A class to work with votings
# By Galkin-Palkin
from typing import List
from AnswerVariant import *


class Voting:
    def __init__(self, name=''):
        self.name = name


class DiscretVoting(Voting):
    def __init__(self, name=''):
        super().__init__(name)
        self.chosen_number: int
        self.first_answer: AnswerVariant()
        self.second_answer: AnswerVariant()


class OneAnswerVoting(Voting):
    def __init__(self, name=''):
        super().__init__(name)
        self.chosen_number = -1
        self.answers: List[AnswerVariant]


class ManyAnswerVoting(Voting):
    def __init__(self, name=''):
        super().__init__(name)
        self.chosen_numbers: List[int]
        self.answers: List[AnswerVariant]
