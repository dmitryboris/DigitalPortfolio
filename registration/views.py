from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from main.models import Profile


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        return super().form_valid(form)


class MyLoginView(LoginView):
    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse(
            'user-detail',
            kwargs={'slug': self.request.user.username.lower()}
        )
