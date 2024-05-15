from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView

from .models import Achievements, Profile


def index(request):
    return render(request, 'main/index.html')


def about(request):
    achievements = Achievements.objects.filter(author=10)
    return render(request, 'main/about.html', {'achievements': achievements})


class UserProfileDetailView(DetailView):
    model = Profile
    template_name = 'main/about.html'
    context_object_name = 'owner'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    # queryset = User.objects.all()


