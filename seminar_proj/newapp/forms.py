from django import forms
import datetime


class ChoiceGameForm(forms.Form):
    game_choice = forms.ChoiceField(choices=[('orel_reshka', 'Орел или решка'), ('cube', 'Кубик'), ('random_num', 'Случайное число')])
    attempt_quantity = forms.IntegerField(min_value=1, max_value=64)
