from django import forms


class DistrictDataUploadForm(forms.Form):

    state_data = forms.FileField(
        widget = forms.FileInput(
            attrs = {
                'id' : 'file-upload'
            }))
    

class MapDataUploadForm(forms.Form):

    map_data = forms.FileField(
        widget = forms.FileInput(
            attrs = {
                'id' : 'file-upload'
            }))