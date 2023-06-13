from .models import Board
from django import forms

class BoardModelForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title','writer','content']
        