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


class ClientModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    login = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    objects = ClientManager()

    @classmethod
    def create(cls, id_num: int, name: str, login: str, email: str, phone: str):
        client = cls(str, id_num, name, login, email, phone)
        return client

    @classmethod
    def is_valid(cls):
        return cls.name != "" and cls.login != "" and cls.email != ""\
                and cls.phone != "" and cls.password != ""


class VotingModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)


class AnswerDataModel(models.Model):
    voting = models.ForeignKey(VotingModel, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()


class AnswerVariantModel(models.Model):
    answer_data = models.ForeignKey(AnswerDataModel, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=64)
    chosen = models.BooleanField()
