from .models import Achievements
from django.forms import ModelForm, TextInput, FileInput


class AchievementForm(ModelForm):
    class Meta:
        model = Achievements
        fields = ['title', 'preview', 'file', ]

        widgets = {
            'title': TextInput(attrs={
                'class': 'field-title',
                'placeholder': 'Над чем вы работали?'
            }),
            'preview': FileInput(attrs={
                'class': 'field-preview',
                'placeholder': 'Загрузите обложку'
            }),
            'file': FileInput(attrs={
                'class': 'field-preview',
                'placeholder': 'Загрузите достижение'
            })
        }