from django.forms import ModelForm
from django.contrib.auth.models import User

class UserForm(ModelForm):
    """Custom new user form for front end"""
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
