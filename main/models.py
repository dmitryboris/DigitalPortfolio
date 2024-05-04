from django.db import models


class Achievements(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    user_id = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date of publication')
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'
