from django.contrib.auth.models import User

from .models import Achievements, Profile
from django.forms import ModelForm, TextInput, FileInput
from django.utils.translation import gettext_lazy as _


class AchievementForm(ModelForm):
    class Meta:
        model = Achievements
        fields = ['title', 'preview', 'file']

        widgets = {
            'title': TextInput(attrs={
                'class': 'project-title',
                'placeholder': 'Над чем вы работали?'
            }),
            'preview': FileInput(attrs={
                'class': 'field-preview',
            }),
            'file': FileInput(attrs={
                'class': 'field-preview',
            })
        }

        # labels = {
        #    'file': _('Загрузите достижение'),
        #    'preview': _('Загрузите обложку')
        # }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('author', None)
        super(AchievementForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.author = User.objects.get(id=self.user.id)
        if commit:
            instance.save()
        return instance


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
