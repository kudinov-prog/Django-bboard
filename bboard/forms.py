from django.forms import ModelForm

from .models import Bd

class Bdform(ModelForm):
    class Meta:
        model = Bd
        fields = ('title', 'content', 'price', 'rubric')
