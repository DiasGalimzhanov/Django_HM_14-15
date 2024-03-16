from django import forms
from .models import VideoCard
import datetime


class VideoCardForm(forms.ModelForm):
    class Meta:
        model = VideoCard
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a name','style': 'width: 30rem;'}),
            'memory': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a memory','style': 'width: 30rem;'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a price','style': 'width: 30rem;'}),
            'manufacturer': forms.Select(attrs={'class': 'form-control', 'style': 'width: 30rem;'}),
            'release_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date', 'class': 'form-control', 'style': 'width: 30rem;'}),
            }
        

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == '':
            raise forms.ValidationError('Name cannot be empty')
        return name
    
    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError('Price cannot be negative')
        return price
    
    def clean_memory(self):
        memory = self.cleaned_data['memory']
        if memory < 1:
            raise forms.ValidationError('Memory cannot be < 1')
        return memory
    
    def clean_release_date(self):
        release_date = self.cleaned_data['release_date']
        if release_date > datetime.date.today():
            raise forms.ValidationError('Release date cannot be in the future')
        return release_date
        

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)


    def clean_search(self):
        search = self.cleaned_data['search']
        if search == '':
            raise forms.ValidationError('Search cannot be empty')
        return search