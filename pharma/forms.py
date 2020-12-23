from django import forms

class StockForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'stock-detail',
                                                         'id':'name',
                                                         'name':'name',
                                                         'placeholder':'Medicine'}))
    
    price = forms.CharField(widget=forms.NumberInput(attrs={'class':'stock-detail',
                                                            'id':'cost',
                                                            'name':'price',
                                                            'placeholder':'100'}))
    
    quantity = forms.CharField(widget=forms.NumberInput(attrs={'class':'stock-detail',
                                                               'id':'amount',
                                                               'name':'quantity',
                                                               'placeholder':'100'}))

class BillForm(forms.Form):
    name =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input',
                                                           'id': 'name',
                                                           'placeholder': 'Name',
                                                           'autofocus': ''}))
    
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class': "form-input",
                                                            'id': 'phone',
                                                            'placeholder': '1234567890',
                                                            'min': 1000000000,
                                                            'max': 9999999999,
                                                            'autofocus': ''}))