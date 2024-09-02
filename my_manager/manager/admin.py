from django.contrib import admin
from .models import Passwords, CryptoWallets, JobOpportunities, MyProjects


class PasswordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'login', 'password', 'secret')

class CryptoWalletsAdmin(admin.ModelAdmin):
    list_display = ('name', 'secret_phrase', 'key', 'password')

class JobOpportunitiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'field_of_activity', 'salary', 'country')

class MyProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'languages', 'time', 'description', 'kind')


admin.site.register(Passwords, PasswordsAdmin)
admin.site.register(CryptoWallets, CryptoWalletsAdmin)
admin.site.register(JobOpportunities, JobOpportunitiesAdmin)
admin.site.register(MyProjects, MyProjectsAdmin)
