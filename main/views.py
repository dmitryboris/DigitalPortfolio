from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView

from .models import Achievements, Profile


def index(request):
    return render(request, 'main/index.html')


def about(request):
    achievements = Achievements.objects.filter(author=10)
    return render(request, 'main/about-dmitry.html', {'achievements': achievements})


class UserProfileDetailView(DetailView):
    model = Profile
    template_name = 'main/about.html'
    context_object_name = 'profile'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context['achievements'] = Achievements.objects.filter(author=profile.user)
        return context

