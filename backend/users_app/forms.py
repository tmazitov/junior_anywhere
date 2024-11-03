from django import forms
from django.contrib.auth.hashers import make_password
from .models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields = ['name', 'second_name', 'email', 'password', 'phone_number']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user