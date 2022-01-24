from django.db import models


class ClientManager(models.Manager):
    def exists_client_with_login(self, login: str):
        for client in self.all():
            if client.login == login:
                return True

        return False

    def get_client_with_login(self, login: str):
        for client in self.all():
            if client.login == login:
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


class ClientModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    login = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    objects = ClientManager()

    @classmethod
    def is_valid(cls):
        return cls.name != "" and cls.login != "" and cls.email != ""\
                and cls.phone != "" and cls.password != ""


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
