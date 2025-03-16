from django.contrib import admin
from .models import Passwords, CryptoWallets, JobOpportunities, MyProjects
# from .models import YourModel, Language
from django import forms
from django.utils.safestring import mark_safe


class PasswordsForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(render_value=True), required=True)

    class Meta:
        model = Passwords
        fields = "__all__"

class PasswordsAdmin(admin.ModelAdmin):
    form = PasswordsForm
    list_display = ('name', 'login', 'password_with_button')

    def password_with_button(self, obj):
        return mark_safe(f'''
            <input type="password" value="{obj.password}" id="password_{obj.id}" readonly style="width: 150px;">
            <button type="button" onclick="togglePassword('password_{obj.id}')">Show</button>
        ''')

    password_with_button.short_description = "Password"

    class Media:
        js = ('admin/js/password_toggle.js',) 

admin.site.register(Passwords, PasswordsAdmin)

class CryptoWalletsAdmin(admin.ModelAdmin):
    list_display = ('name', 'secret_phrase', 'key', 'password')

class JobOpportunitiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'field_of_activity', 'salary', 'country')

class MyProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'languages', 'time', 'description', 'kind')

# Created a programming language selection

# class YourModelForm(forms.ModelForm):
#     class Meta:
#         model = YourModel
#         fields = ['primary_language', 'additional_languages']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['primary_language'].widget.attrs.update({'style': 'width: 50%; display: inline-block;'})
#         self.fields['additional_languages'].widget.attrs.update({'style': 'width: 50%; display: inline-block;'})

# class YourModelAdmin(admin.ModelAdmin):
#     form = YourModelForm
#     fieldsets = (
#         (None, {
#             'fields': (('primary_language', 'additional_languages'),)
#         }),
#     )

# admin.site.register(YourModel, YourModelAdmin)
# admin.site.register(Language)

admin.site.register(CryptoWallets, CryptoWalletsAdmin)
admin.site.register(JobOpportunities, JobOpportunitiesAdmin)
admin.site.register(MyProjects, MyProjectsAdmin)
