from django.db import models

def title_(self, obj):
    from django.utils.html import format_html
    return format_html(
        f'<div style="width: 50px; word-wrap: break-word">{obj.title}</div>'
    )

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
