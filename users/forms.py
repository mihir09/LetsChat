from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from crispy_forms.helper import FormHelper

class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


        email = forms.EmailField()
        self.fields['username'].help_text = '\n'
        self.fields['email'].help_text = '\n'
        self.fields['password1'].help_text = 'Your password must contain at least 8 characters.'
        self.fields['password2'].help_text = '\n'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']


from django import forms



