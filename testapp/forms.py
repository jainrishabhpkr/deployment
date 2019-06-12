from django import forms

class Inputform(forms.Form):
    input = forms.IntegerField(label='enter a number')
