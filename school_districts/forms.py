from django import forms


class DataUploadForm(forms.Form):

    state_data = forms.FileField()