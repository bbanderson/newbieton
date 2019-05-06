from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'food_name',
            'food_ingredient',
            'food_img',
            'recipe_description',
            'cooking_time'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'food_title', 'placeholder':'입력하세요'}),
            'food_name': forms.TextInput(attrs={'class': 'food_name'}),
            'food_ingredient' : forms.TextInput(attrs={'class': 'food_ingredient'}),
            'food_img' : forms.FileInput(attrs={'class': 'food_img'}),
            'recipe_description' : forms.TextInput(attrs={'class': 'recipe_description'}),
            'cooking_time' : forms.TextInput(attrs={'class': 'cooking_time'}),
            
        }
        labels = {
            'title': '닉네임',
            'food_name': '이메일',
            'food_ingredient': '패스워드'
        }