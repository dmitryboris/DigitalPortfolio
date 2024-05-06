from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import RegisterForm


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
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
