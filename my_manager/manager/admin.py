from django.contrib import admin
from .models import Passwords, CryptoWallets, JobOpportunities

class PasswordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'login', 'password', 'secret')

class CryptoWalletsAdmin(admin.ModelAdmin):
    list_display = ('name', 'secret_phrase', 'key', 'password')

class JobOpportunitiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'field_of_activity', 'salary', 'country')

admin.site.register(Passwords, PasswordsAdmin)
admin.site.register(CryptoWallets, CryptoWalletsAdmin)
admin.site.register(JobOpportunities, JobOpportunitiesAdmin)
