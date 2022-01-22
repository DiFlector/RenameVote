from first.backend.Voting import *


class Client:
    def __init__(self, name: str, client_id: int, phone: str, login: str, email: str, description=''):
        self.name = name
        self.login = login
        self.description = description
        self.phone = phone
        self.email = email

        # Server data
        self.voting_indexes = List[int]
        self.answers = List[AnswerData]
        self.id = client_id

    def change_name(self, name: str):
        self.name = name

    def change_description(self, descript: str):
        self.description = descript

    def add_voting(self, index: int):
        self.votings_indexes.append(index)

    def add_answer_data(self, voting_index: int, date: datetime, answers: List[AnswerVariant]):
        self.answers.append(AnswerData(voting_index, date, answers))

    def get_votings(self, database):
        res = []

        for voting in database.votings:
            if voting.id in self.votings_indexes:
                res.append(voting)

        return res

    def check_client(self):
        return len(self.name) > 0 and len(self.login) > 0 and len(self.email) > 0 and self.id >= 0 and len(self.phone)
