from django import forms
import datetime


class UpdateProdForm(forms.Form):

    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Наименование продукта'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.DecimalField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Количество товара'}))
    added_date = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Дата поступления товара'}))
    image = forms.ImageField()
    

class ImageForm(forms.Form):
    image = forms.ImageField()

