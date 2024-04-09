from django.contrib import admin
from .models import Passwords, CryptoWallets

class PasswordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'login', 'password', 'secret')

class CryptoWalletsAdmin(admin.ModelAdmin):
    list_display = ('name', 'secret_phrase', 'key', 'password')

admin.site.register(Passwords, PasswordsAdmin)
admin.site.register(CryptoWallets, CryptoWalletsAdmin)
