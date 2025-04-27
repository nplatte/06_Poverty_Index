from django import forms


class DistrictDataUploadForm(forms.Form):

    state_data = forms.FileField()