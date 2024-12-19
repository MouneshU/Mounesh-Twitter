from django import forms
from tweetapp.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
    
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['Text', 'photo']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
