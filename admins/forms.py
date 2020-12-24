from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from patients.models import Patient


# Overriding the default authentication form
class AuthForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-input',
                                                           'id': 'username',
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
            'name': forms.TextInput(attrs={'class': 'form-input',
                                           'id': 'name',
                                           'placeholder': 'Name',
                                           'autofocus': ''}),
            'age': forms.NumberInput(attrs={'class': 'form-input',
                                            'id': 'age',
                                            'placeholder': '100',
                                            'min': 0,
                                            'max': 150,
                                            'autofocus': ''}),
            'gender': forms.Select(choices=Patient.gender_list, attrs={'class': 'form-input-dropdown',
                                                                       'id': 'gender',
                                                                       'autofocus': ''}),
            'blood_type': forms.Select(choices=Patient.blood_types, attrs={'class': 'form-input-dropdown',
                                                                           'id': 'blood_type',
                                                                           'autofocus': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-input',
                                             'id': 'email',
                                             'placeholder': 'example@email.com',
                                             'autofocus': ''}),
            'phone': forms.NumberInput(attrs={'class': 'form-input',
                                              'id': 'phone',
                                              'min': 1000000000,
                                              'max': 9999999999,
                                              'placeholder': '1234567890',
                                              'autofocus': ''})
        }
