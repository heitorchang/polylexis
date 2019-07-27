from django import forms

class TextFileForm(forms.Form):
    contents = forms.CharField(widget=forms.Textarea)
