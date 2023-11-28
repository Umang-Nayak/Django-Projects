from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(initial="UMA", help_text="30 character only")
