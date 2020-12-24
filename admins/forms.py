from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from patients.models import Patient


# Overriding the default authentication form
class AuthForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"class": "form-input",
                                                           "id": "username",
                                                           'placeholder': 'username',
                                                           'autofocus': ''}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                          'class': 'form-input',
                                          'id': 'password',
                                          'placeholder': 'password',
                                          'autofocus': ''}))


# Creating new patient form
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={}),
            'age': forms.NumberInput(attrs={}),
            'gender': forms.Select(choices=Patient.gender_list, attrs={}),
            'blood_type': forms.Select(choices=Patient.blood_types, attrs={}),
            'email': forms.TextInput(attrs={}),
            'phone': forms.NumberInput(attrs={})
        }
