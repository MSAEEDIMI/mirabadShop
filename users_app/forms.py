from django import forms
from django.contrib.auth.models import User
from products_app.models import Product
class Regestrform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name',"image")
        widgets = {
        'name': forms.TextInput(attrs={"class":"form-group"}),

        }