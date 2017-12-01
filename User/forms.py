from django import forms
from django.core.validators import EmailValidator

field = [
    {
        "id": "name",
        "name": "name",
        "label": "input",
        "default": None,
        "elements": [
            { "class": "form-control" },
            { "type": "text" },
            { "placeholder": "Name" }
        ]
    },
    {
        "id": "email",
        "name": "email",
        "default": None,
        "label": "input",
        "elemets": [
            { "class": "form-control" },
            { "type": "text" },
            { "placeholder": "Email" }
        ]
    },
    {
        "id": "account",
        "name": "account",
        "label": "input",
        "default": None,
        "elements": [
           { "class": "form-control" },
           { "type": "text" },
           { "placeholder": "Account" }
        ]
    },
    {
        "id": "status",
        "name": "status",
        "label": ""
    }
]

form = [
    {"AddUserForm": ["name", "email", "account"]},
    {"ModUserForm": ["name", "email"]},
    {"DelUserForm": ["account"]}
]


class ModUserForm(forms.Form):
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
    account = forms.CharField(label="Account", required=True, widget=forms.TextInput(attrs=
      {
        'id': 'account',
        'class' : 'form-control',
        'placeholder': 'Account',
        'type': 'text'
      }
    ))

class AddUserForm(forms.Form):
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
