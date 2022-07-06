from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import gettext
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import SignUpForm


# def index(request):
#     return render(request, 'index.html', context={})


class HomeView(TemplateView):
    template_name = "index.html"


class UserCreateView(FormView):
    
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(UserCreateView, self).form_valid(form)


class LoginView(TemplateView):
    template_name = "login.html"

    def post(self, *args, **kwargs):
        pass


class LogoutView(TemplateView):
    def post(self, *args, **kwargs):
        pass
