from first.backend.Voting import Voting
from first.backend.Client import Client
from typing import List


class Database:
    def __init__(self):
        self.votings = []
        self.clients = []

    def update(self):
        pass

    def add_client(self, client: Client):
        self.clients.append(client)

    def create_client(self, name: str, phone: str, login: str, email: str):
        return Client(name, 0, phone, login, email)

    def add_voting(self, voting: Voting):
        voting.id = len(self.votings)
        self.votings.append(voting)

    def exists_with_login(self, login: str):
        for client in self.clients:
            if client.login == login:
                return True

        return False


database = Database()
