# Generated by Django 5.0.1 on 2024-01-08 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_customuser_saldo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='saldo',
            field=models.IntegerField(default=0),
        ),
    ]
