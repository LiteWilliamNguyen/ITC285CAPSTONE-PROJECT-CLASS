from django import forms
from .models import Product, Monk, Member

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class MonkForm(forms.ModelForm):
    class Meta:
        model=Monk
        fields='__all__'

class MemberForm(forms.ModelForm):
    class Meta:
        model=Member
        fields='__all__'

