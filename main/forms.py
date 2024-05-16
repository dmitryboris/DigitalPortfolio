from .models import Achievements, Profile
from django.forms import ModelForm, TextInput, FileInput
from django.utils.translation import gettext_lazy as _


class AchievementForm(ModelForm):
    class Meta:
        model = Achievements
        fields = ['title', 'preview', 'file', 'author']

        widgets = {
            'title': TextInput(attrs={
                'class': 'field-title',
                'placeholder': 'Над чем вы работали?'
            }),
            'preview': FileInput(attrs={
                'class': 'field-preview',
            }),
            'file': FileInput(attrs={
                'class': 'field-preview',
            })
        }

        labels = {
            'file': _('Загрузите достижение'),
            'preview': _('Загрузите обложку')
        }

    def __init__(self, *args, **kwargs):
        super(AchievementForm, self).__init__(*args, **kwargs)
        self.fields['file'].label = 'Загрузите достижение'
        self.fields['preview'].label = 'Загрузите обложку'


class SearchProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['slug']

        widgets = {
            'slug': TextInput(attrs={
                'class': 'field-title',
                'placeholder': 'Ник пользователя'
            })
        }
