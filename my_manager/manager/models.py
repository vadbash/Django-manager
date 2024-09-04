from django.db import models

class Passwords(models.Model):
    name = models.CharField('Name of app', max_length = 500)
    login = models.CharField('Login', max_length = 500)
    password = models.CharField('Password', max_length = 500)
    secret = models.CharField('Secret phrase', max_length = 500, blank=True)

    class Meta:
        verbose_name = "Password"
        verbose_name_plural = "Passwords"


class CryptoWallets(models.Model):
    name = models.CharField('Wallet name', max_length = 500)
    secret_phrase = models.CharField('Secret phrase', max_length = 500, blank=True)
    key = models.CharField('Private key', max_length = 500, blank=True)
    password = models.CharField('Password', max_length = 500, blank=True)

    class Meta:
        verbose_name = "Crypto Wallet"
        verbose_name_plural = "Crypto Wallets"

class JobOpportunities(models.Model):
    name = models.CharField('Name of company', max_length=500)
    field_of_activity = models.CharField('Field of activity', max_length=500, blank=True)
    salary = models.CharField('Salary', max_length=500, blank=True)
    country = models.CharField('Country of office', max_length=500, blank=True)

    class Meta:
        verbose_name = "Job Opportunity"
        verbose_name_plural = "Job Opportunities"
    
class MyProjects(models.Model):
    name = models.CharField('Project name', max_length=500)
    languages = models.CharField('Languages that you will use', max_length=500)
    time = models.DateField('Duration')
    description = models.TextField('Brief description', max_length=1000, blank=True)
    kind = models.CharField('Kind of your project', max_length=500, blank=True)

    class Meta:
        verbose_name = "My Project"
        verbose_name_plural = "My Projects"



# Created a programming language selection 

# class Language(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

# class YourModel(models.Model):
#     primary_language = models.ForeignKey(Language, related_name='primary_language', on_delete=models.CASCADE)
#     additional_languages = models.ManyToManyField(Language, related_name='additional_languages', blank=True)

#     def __str__(self):
#         return f"Primary: {self.primary_language.name}, Additional: {[lang.name for lang in self.additional_languages.all()]}"
