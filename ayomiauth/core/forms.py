from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ['email']

class EmailForm(forms.Form):
    email = forms.EmailField(label="Your new email", required=True)