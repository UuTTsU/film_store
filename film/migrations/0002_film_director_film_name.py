# Generated by Django 4.2.11 on 2024-05-18 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='director',
            field=models.CharField(default='some director', max_length=250),
        ),
        migrations.AddField(
            model_name='film',
            name='name',
            field=models.CharField(default='film_name', max_length=250),
        ),
    ]
