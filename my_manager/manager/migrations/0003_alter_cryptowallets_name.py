# Generated by Django 5.0.3 on 2024-03-22 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_cryptowallets_alter_passwords_secret'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptowallets',
            name='name',
            field=models.CharField(max_length=500, verbose_name='Wallet name'),
        ),
    ]
