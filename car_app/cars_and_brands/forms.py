from django import forms
from .models import Brand, Car

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('brand_name',)

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('brand', 'model')
