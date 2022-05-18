from django import forms
from django.forms import ModelForm
from post.models import LostPet

class postForm(ModelForm):
    animal_image = forms.FileField
    class Meta:
        model = LostPet
        fields = ['pub_date', 'pub_name','pub_phone','pub_email','animal_type','animal_status','animal_location','animal_freetext','animal_image']