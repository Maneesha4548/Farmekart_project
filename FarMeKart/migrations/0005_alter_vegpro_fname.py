# Generated by Django 3.2.1 on 2021-06-03 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarMeKart', '0004_auto_20210603_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vegpro',
            name='fname',
            field=models.CharField(max_length=20),
        ),
    ]
