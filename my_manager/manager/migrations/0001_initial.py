# Generated by Django 5.0.3 on 2024-03-22 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passwords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Name of app')),
                ('login', models.CharField(max_length=500, verbose_name='Login')),
                ('password', models.CharField(max_length=500, verbose_name='Password')),
                ('secret', models.CharField(max_length=500, verbose_name='secret phrase')),
            ],
            options={
                'verbose_name': 'Password',
                'verbose_name_plural': 'Passwords',
            },
        ),
    ]