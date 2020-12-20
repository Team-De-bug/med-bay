from django import forms


# Case processing form
class CaseProcessing(forms.Form):
    has_pres = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': "patient-detail",
                                                                    'id': "has-prescription",
                                                                    'name': "has-prescription",
                                                                    'type': "checkbox",
                                                                    'default': "false"}), required=False)

    desc = forms.CharField(widget=forms.Textarea(attrs={'class': "patient-detail",
                                                        'id': "diagnosis",
                                                        'cols': "16", 'rows': "5",
                                                        'name': "diagnosis",
                                                        'placeholder': "Your Diagnosis"}))
