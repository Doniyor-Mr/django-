from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError

class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields = ['title','contact','is_published','category']
        widgets= {
            'title':forms.TextInput(attrs={"class":'form-control'}),
            'contact':forms.Textarea(attrs={"class":'form-control', "rows":5 }),
            'category':forms.Select(attrs={"class":'form-control'})
        }

    def clean_title(self):
        title =self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('boshi  boshlanmasin  son bilan')
        return title