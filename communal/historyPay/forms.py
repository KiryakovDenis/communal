from django import forms

class periodForm(forms.Form):
    name = forms.CharField()
    begin_d = forms.DateField()
    end_d   = forms.DateField()
    comment = forms.CharField(widget=forms.Textarea)