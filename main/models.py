from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Achievements(models.Model):
    title = models.CharField(max_length=50)
    preview = models.ImageField(
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
        ]
    )
    file = models.FileField(
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'pdf']),
        ]
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    objects = models.Manager()

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
