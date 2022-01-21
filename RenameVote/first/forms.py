from django import forms


class RegistrationForm(forms.Form):
    name = forms.CharField()
    login = forms.CharField()
    email = forms.CharField()
    phone = forms.CharField()
    password = forms.CharField()
    confirm_password = forms.CharField()
