from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.text import slugify
from django.views.decorators.http import require_POST
from django.views.generic import DetailView
from .forms import AchievementForm, ProfileForm
from .models import Achievements, Profile
from django.http import HttpResponseForbidden, JsonResponse
from functools import wraps


def user_is_owner(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        username = kwargs.get('slug')
        print(f"URL username: {username}, Logged in username: {request.user.username}")
        if request.user.is_authenticated and slugify(request.user.username) == username:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You are not allowed to access this page.")

    return _wrapped_view


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

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if query:
            try:
                user = User.objects.get(username=query)
                return redirect(reverse('user-detail', kwargs={'slug': slugify(user.username)}))
            except Exception:
                pass
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context['achievements'] = Achievements.objects.filter(author=profile.user)
        return context


@login_required
@user_is_owner
def create_achievement(request, slug):
    error = ''
    if request.method == 'POST':
        form = AchievementForm(request.POST, request.FILES, author=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('user-detail', kwargs={'slug': slug}))
        else:
            error = 'Ошибка загрузки файлов'

    form = AchievementForm(author=request.user)

    data = {
        'form': form,
        'slug': slug,
        'error': error
    }

    return render(request, 'main/add.html', data)


def increment_views(request, pk):
    achievement = Achievements.objects.get(pk=pk)
    achievement.views += 1
    achievement.save()
    return redirect(reverse('achievement-detail', kwargs={'pk': pk}))


@require_POST
def toggle_like(request, pk):
    achievement = Achievements.objects.get(pk=pk)
    if request.user in achievement.liked_by.all():
        achievement.liked_by.remove(request.user)
        achievement.likes -= 1
        liked = False
    else:
        achievement.liked_by.add(request.user)
        achievement.likes += 1
        liked = True
    achievement.save()
    return JsonResponse({'likes': achievement.likes, 'liked': liked})


@login_required
@user_is_owner
def update_profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('user-detail', kwargs={'slug': slug}))
    else:
        form = ProfileForm(instance=profile)

    return redirect(reverse('user-detail', kwargs={'slug': slug}))


@login_required
def redirect_home(request, pk):
    user = User.objects.get(pk=pk)
    return redirect(reverse('user-detail', kwargs={'slug': slugify(user.username)}))


def achievement_detail(request, pk):
    achievement = Achievements.objects.get(pk=pk)
    return render(request, 'main/achievement.html', {'achievement': achievement})