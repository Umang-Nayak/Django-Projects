from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(label="Your Name",
                           label_suffix=" ",
                           initial="UMA",
                           required=False,
                           disabled=True,
                           help_text="Limit 30 Character")
