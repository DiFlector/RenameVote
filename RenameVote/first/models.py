from django.db import models
from django.contrib.auth.models import User, UserManager


class ClientManager(UserManager):
    def exists_client_with_login(self, login: str):
        for client in self.all():
            if client.login2 == login:
                return True

        return False

    def get_client_with_login(self, login: str):
        for client in self.all():
            if client.login2 == login:
                return client

        return None

    def exists_client_with_id(self, index: int):
        for client in self.all():
            if client.id == index:
                return True

        return False

    def get_client_with_id(self, index: int):
        for client in self.all():
            if client.id == index:
                return client

        return None


class ClientModel(User):
    name2 = models.CharField(max_length=64)
    phone2 = models.CharField(max_length=32)
    login2 = models.CharField(max_length=64)
    email2 = models.EmailField()
    password2 = models.CharField(max_length=64)
    objects = ClientManager()
    registration_date = models.DateTimeField()

    @classmethod
    def is_valid(cls):
        return cls.name2 != "" and cls.login2 != "" and cls.email2 != ""\
                and cls.phone2 != "" and cls.password2 != ""


class AnswerHistoryModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    voting_id = models.IntegerField()
    date = models.DateTimeField()


class AnswerHistoryElementModel(models.Model):
    history = models.ForeignKey(AnswerHistoryModel, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    index = models.IntegerField()


class VotingModel(models.Model):
    type = models.BooleanField()
    id = models.IntegerField(primary_key=True)
    owner_id = models.IntegerField()
    name = models.CharField(max_length=128)
    date = models.DateTimeField()

    @classmethod
    def is_valid(cls):
        return name != '' and owner_id >= -1


class AnswerVariantModel(models.Model):
    voting = models.ForeignKey(VotingModel, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=64)


class AnswerDataModel(models.Model):
    id = models.IntegerField(primary_key=True)
    answer = models.ForeignKey(AnswerVariantModel, on_delete=models.CASCADE)
    voted_client_id = models.IntegerField()
