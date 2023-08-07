from django.contrib.auth.models import User
from django.forms import ModelForm
from django import  forms


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password')
        
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=32)

