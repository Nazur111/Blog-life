from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm  # кастомна форма для реєстрації


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "Autenfication/register.html"
    success_url = reverse_lazy("login")  # після успішної реєстрації переходить на логін


class UserLoginView(LoginView):
    template_name = "Autenfication/login.html"
    authentication_form = AuthenticationForm  # використовуємо стандартну форму для уникнення CSRF проблем

    def get_success_url(self):
        return reverse_lazy("home")  # редірект після логіну



class UserLogoutView(LogoutView):
    next_page = reverse_lazy("home")

    # Дозволити GET

