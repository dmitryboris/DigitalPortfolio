from django import template

register = template.Library()


@register.filter(name='file_ext')
def file_ext(url, ext):
    return url.lower().endswith(ext)


@register.filter(name='liked')
def file_ext(user, achievement):
    return user in achievement.liked_by.all()
