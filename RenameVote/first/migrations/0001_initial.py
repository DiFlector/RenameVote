# Generated by Django 4.0.1 on 2022-01-26 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import first.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name2', models.CharField(max_length=64)),
                ('phone2', models.CharField(max_length=32)),
                ('login2', models.CharField(max_length=64)),
                ('email2', models.EmailField(max_length=254)),
                ('password2', models.CharField(max_length=64)),
                ('registration_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', first.models.ClientManager()),
            ],
        ),
        migrations.CreateModel(
            name='VotingModel',
            fields=[
                ('type', models.BooleanField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('owner_id', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='AnswerVariantModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=64)),
                ('voting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.votingmodel')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerHistoryModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('voting_id', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.clientmodel')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerHistoryElementModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('index', models.IntegerField()),
                ('history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.answerhistorymodel')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerDataModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('voted_client_id', models.IntegerField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.answervariantmodel')),
            ],
        ),
    ]
