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
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'pdf', 'ogg', 'mp3']),
        ]
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500, null=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    liked_by = models.ManyToManyField(User, related_name='liked_achievements', blank=True)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )

    objects = models.Manager()

    def formatted_likes(self):
        return format_number_with_suffix(self.likes)

    def formatted_views(self):
        return format_number_with_suffix(self.views)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    is_private = models.BooleanField(default=False)
    avatar = models.ImageField(
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
        ]
    )

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


def format_number_with_suffix(value):
    if value >= 1000:
        return f"{value // 1000}k"
    else:
        return str(value)
