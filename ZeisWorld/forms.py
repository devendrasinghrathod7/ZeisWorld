from django import forms


class Students(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    