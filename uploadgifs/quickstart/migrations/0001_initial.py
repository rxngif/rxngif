# Generated by Django 2.2.7 on 2019-11-18 23:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gifs',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
            ],
        ),
    ]
