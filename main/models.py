from django.conf import settings
from django.db import models


class Achievements(models.Model):
    title = models.CharField(max_length=50)
    preview = models.ImageField(null=True)
    file = models.FileField()
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'
