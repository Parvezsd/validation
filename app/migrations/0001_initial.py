# Generated by Django 5.0.7 on 2024-11-05 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=100)),
                ('semail', models.EmailField(max_length=254)),
            ],
        ),
    ]
