# Generated by Django 5.0.1 on 2024-01-19 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_alter_customuser_elapsed_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_saque_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
