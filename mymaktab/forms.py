from django import forms
from .models import Oblast, LanguageEducation

class SearchSchoolForm(forms.Form):
    oblast = forms.ChoiceField(
        required=True,
        label="ОБЛАСТЬ",
        initial='',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    region = forms.ChoiceField(
        choices=[],
        required=True,
        label="РЕГИОН",
        initial='',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    neighborhood = forms.ChoiceField(
        choices=[],
        required=True,
        label="СХОДЫ ГРАЖДАН МАХАЛЛЕЙ",
        initial='',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    street = forms.ChoiceField(
        choices=[],
        required=True,
        label="УЛИЦА",
        initial='',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    house = forms.ChoiceField(
        choices=[],
        required=True,
        label="ДОМ",
        initial='',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    lang_edu = forms.ChoiceField(
        required=True,
        label="ЯЗЫК ОБУЧЕНИЯ",
        initial='',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super(SearchSchoolForm, self).__init__(*args, **kwargs)
        self.fields['oblast'].choices = [(o.id, o.name) for o in Oblast.objects.all()]
        self.fields['lang_edu'].choices = [(l.id, l.name) for l in LanguageEducation.objects.all()]
