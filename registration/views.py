from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView

from dPortfolio import settings
from .forms import RegisterForm, LoginForm


def login(request):
    return render(request, 'registration/login.html')


def register(request):
    return render(request, 'registration/register.html')


def password_reset(request):
    return render(request, 'registration/password_reset.html')


@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('user-detail')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserDetailView(DetailView):
    model = settings.AUTH_USER_MODEL
    template_name = 'registration/profile.html'
    context_object_name = 'owner'


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            from django.urls import reverse
            return redirect(reverse('user-detail', kwargs={'username': user.username}))
        else:
            # Обработка случая неверного имени пользователя или пароля
            pass
    return render(request, 'login.html')
