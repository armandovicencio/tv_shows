from django import forms
from shows.models import Show


class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['title','network', 'release_date', 'description' ]
        labels = {
            'title': 'Title',
            'network': 'Network',
            'release_date': 'Release Date',
            'description': 'Description'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'network': forms.TextInput(attrs={'class': 'form-control'}),
            'release_date': forms.DateInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
            
            
            
    