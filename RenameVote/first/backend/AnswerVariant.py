from datetime import datetime
from typing import List


class AnswerVariant:
    def __init__(self, text='', is_chosen=False):
        self.text = text
        self.chosen = is_chosen


class AnswerData:
    def __init__(self, index: int, date: datetime, answers: List[AnswerVariant]):
        self.voting_index = index
        self.answers: answers
        self.date = date
