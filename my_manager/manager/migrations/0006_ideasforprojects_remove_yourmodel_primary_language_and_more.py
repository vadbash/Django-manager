# Generated by Django 5.0.3 on 2024-09-02 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_language_alter_jobopportunities_country_yourmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdeasForProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Name for your project')),
                ('languages', models.CharField(max_length=500, verbose_name='Languages that you will use')),
                ('time', models.DateField(verbose_name='Duration of your project')),
                ('description', models.TextField(blank=True, max_length=1000, verbose_name='Brief description')),
                ('kind', models.CharField(blank=True, max_length=500, verbose_name='Kind of your project')),
            ],
        ),
        migrations.RemoveField(
            model_name='yourmodel',
            name='primary_language',
        ),
        migrations.RemoveField(
            model_name='yourmodel',
            name='additional_languages',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='YourModel',
        ),
    ]