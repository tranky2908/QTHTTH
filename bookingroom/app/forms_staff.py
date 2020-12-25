from django import forms
from .models import *


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['status']

class CreateAccountStaffForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

class CreateAccountUserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'