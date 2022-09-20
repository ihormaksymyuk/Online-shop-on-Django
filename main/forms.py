
from .models import Catalog
from django.forms import ModelForm, TextInput, Textarea

class CatalogForm(ModelForm):
    class Meta:
        model = Catalog
        fields = ['title', 'description', 'price']
        widgets = {
            "title": TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': 'Введіть назву товару'
                }
            ),
            "description": Textarea(
                attrs={
                    'class': "form-control",
                    'placeholder': 'Додайте опис товару'
                }
            ),
            "price": TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': 'Введіть ціну товару'
                }
            ),
        }
