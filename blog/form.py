from django import forms
from .models import Blog, BuyItem, SellItem

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']

class SellItemPost(forms.ModelForm):
    class Meta :
        model = SellItem
        fields = ['title', 'sell_image', 'body']