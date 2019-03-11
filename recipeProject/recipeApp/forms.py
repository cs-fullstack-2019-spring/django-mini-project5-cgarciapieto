from django import forms
from .models import RecipeModel, NewProfileModel
from datetime import date


class newProfileForm(forms.ModelForm):
    class Meta:
        model = NewProfileModel
        fields=["name", 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords must match!")

class RecipeForm(forms.ModelForm):
    class Meta:
        model   = RecipeModel
        exclude = [
            'foreignkeyToNewProfile']


