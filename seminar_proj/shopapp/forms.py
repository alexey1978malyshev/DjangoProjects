from django import forms
import datetime
from .models import Image
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify


class UpdateProdForm(forms.Form):

    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Наименование продукта'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.DecimalField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Количество товара'}))
    added_date = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Дата поступления товара'}))
    #image = forms.ImageField()
    

class ImageForm(forms.Form):
    image = forms.ImageField()


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {'url': forms.HiddenInput, }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not match valid image extensions.')
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super(ImageCreateForm, self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = '{}.{}'.format(slugify(image.title), image_url.rsplit('.', 1)[1].lower())

        # download image from the given URL
        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)
        if commit:
            image.save()
        return image

