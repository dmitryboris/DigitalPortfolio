from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, DetailView
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'

    def get_success_url(self):
        return reverse(
            'user-detail',
            kwargs={'username': self.request.user.username}
        )

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class MyLoginView(LoginView):
    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse(
            'user-detail',
            kwargs={'username': self.request.user.username}
        )
