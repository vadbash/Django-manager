# Generated by Django 5.0.3 on 2024-03-22 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoWallets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Name of app')),
                ('secret_phrase', models.CharField(blank=True, max_length=500, verbose_name='Secret phrase')),
                ('key', models.CharField(blank=True, max_length=500, verbose_name='Private key')),
                ('password', models.CharField(blank=True, max_length=500, verbose_name='Password')),
            ],
            options={
                'verbose_name': 'Crypto Wallet',
                'verbose_name_plural': 'Crypto Wallets',
            },
        ),
        migrations.AlterField(
            model_name='passwords',
            name='secret',
            field=models.CharField(blank=True, max_length=500, verbose_name='Secret phrase'),
        ),
    ]