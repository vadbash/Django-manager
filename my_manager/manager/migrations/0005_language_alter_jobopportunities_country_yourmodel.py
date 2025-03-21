# Generated by Django 5.0.3 on 2024-09-02 19:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_jobopportunities'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='jobopportunities',
            name='country',
            field=models.CharField(blank=True, max_length=500, verbose_name='Country of office'),
        ),
        migrations.CreateModel(
            name='YourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_languages', models.ManyToManyField(blank=True, related_name='additional_languages', to='manager.language')),
                ('primary_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_language', to='manager.language')),
            ],
        ),
    ]
