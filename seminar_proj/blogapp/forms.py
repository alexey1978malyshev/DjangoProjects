from django import forms
import datetime


class AddNewAuthor(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите имя автора'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите фамиплию автора'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    biography = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    birthday = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control',
                                                                                          'type': 'date'}))  # устанавливаем календарик
