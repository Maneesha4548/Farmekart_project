# Generated by Django 3.2.1 on 2021-05-31 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FarMeKart', '0002_auto_20210531_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='veg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FarMeKart.userpro'),
        ),
    ]
