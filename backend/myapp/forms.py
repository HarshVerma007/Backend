from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
#     # fields=['image']
    class Meta:
        model= Image
        fields = '__all__'
        labels = {'photo': ""}

