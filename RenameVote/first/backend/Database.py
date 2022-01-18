from Voting import *
from Client import Client


class Database:
    def __init__(self):
        self.votings = List[Voting]
        self.clients = List[Client]

    def update(self):
        pass

    def add_client(self, name: str, descript: str):
        self.clients.append(Client(name, len(self.clients), descript))

    def add_voting(self, voting: Voting):
        voting.id = len(self.votings)
        self.votings.append(voting)


database = Database
