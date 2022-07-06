from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import gettext


# def index(request):
#     return render(request, 'index.html', context={})


class HomeView(TemplateView):
    template_name = "index.html"


class UserCreateView(TemplateView):
    template_name = "register.html"

    def post(self, *args, **kwargs):
        pass


class LoginView(TemplateView):
    template_name = "login.html"

    def post(self, *args, **kwargs):
        pass


class LogoutView(TemplateView):
    def post(self, *args, **kwargs):
        pass
