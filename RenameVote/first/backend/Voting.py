from first.backend.AnswerVariant import *


class Voting:
    def __init__(self, voting_id: int, owner_id: int, name=''):
        self.name = name
        self.answers: List[AnswerVariant]
        self.id = voting_id
        self.owner_id = owner_id


class DiscretVoting(Voting):
    def __init__(self, voting_id: int, owner_id: int, name=''):
        super().__init__(voting_id, owner_id, name)
        self.chosen_number: int


class OneAnswerVoting(Voting):
    def __init__(self, voting_id: int, owner_id: int, name=''):
        super().__init__(voting_id, owner_id, name)
        self.chosen_number: int


class ManyAnswerVoting(Voting):
    def __init__(self, voting_id: int, owner_id: int, name=''):
        super().__init__(voting_id, owner_id, name)
        self.chosen_numbers: List[int]
