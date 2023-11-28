from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'css1', 'id': 'uniqueid'}))
