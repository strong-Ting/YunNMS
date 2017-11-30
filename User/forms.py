from django import forms
from django.core.validators import EmailValidator

class AddUserForm(forms.Form):
    account = forms.CharField(label="Account", required=True, widget=forms.TextInput(attrs=
      {
        'id': 'account',
        'class' : 'form-control',
        'placeholder': 'Account',
        'type': 'text'
      }
    ))
    passwd = forms.CharField(label="Passwd", required=False, widget=forms.TextInput(attrs=
      {
        'id': 'passwd',
        'class': 'form-control',
        'disabled': 'disabled',
        'type': 'password'
      }
    ))
    passPreset = forms.CharField(required=False, widget=forms.TextInput(attrs=
      {
        'class': 'form-control',
        'type': 'checkbox',
        'onclick': 'edit_passwd(this)'
      }
    ))
    name = forms.CharField(label="Name", required=True, widget=forms.TextInput(attrs=
      {
        'id': 'name',
        'class': 'form-control',
        'placeholder': 'Name',
        'type': 'text'
      }
    ))
    email = forms.EmailField(label="Email", required=True, widget=forms.TextInput(attrs=
      {
        'id': 'email',
        'class': 'form-control',
        'placeholder': 'Email',
        'type': 'text'
      }
    ),validators=[EmailValidator()])
    