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
    
