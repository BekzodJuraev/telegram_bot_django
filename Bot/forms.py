from django import forms
from .models import Add_item

class Create_item(forms.ModelForm):
    class Meta:
        model=Add_item
        fields = ['image', 'price', 'name']
