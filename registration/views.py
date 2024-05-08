from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView
from django.conf import settings
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User

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
    model = User
    template_name = 'registration/profile.html'
    context_object_name = 'owner'
    queryset = User.objects.all()
