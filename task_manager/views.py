from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
# from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
# from django.contrib.auth.forms import UserCreationForm
# from django.utils.translation import gettext
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import SignUpForm


class HomeView(TemplateView):
    
    template_name = "index.html"


class UsersView(ListView):
    
    template_name = "users.html"
    model = User
    context_object_name = 'users'
    paginate_by = 10


class UserCreateView(CreateView):

    model = User
    form_class = SignUpForm
    template_name = "register.html"
    success_url = reverse_lazy('login')


# class UserCreateView(FormView):
    
#     form_class = SignUpForm
#     success_url = reverse_lazy('login')
#     template_name = "register.html"

#     def form_valid(self, form):
#         form.save()
#         return super(UserCreateView, self).form_valid(form)


class LoginView(TemplateView):
    
    template_name = "login.html"

    def post(self, *args, **kwargs):
        pass


class LogoutView(TemplateView):
    
    def post(self, *args, **kwargs):
        pass
