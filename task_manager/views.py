# from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.contrib.messages.views import SuccessMessageMixin


class HomeView(TemplateView):
    
    template_name = "index.html"


class UsersView(ListView):
    
    template_name = "users.html"
    model = User
    context_object_name = 'users'
    paginate_by = 10


class UserCreateView(SuccessMessageMixin, CreateView):

    model = User
    form_class = SignUpForm
    template_name = "register.html"
    success_url = reverse_lazy('login')
    success_message = _("Пользователь успешно зарегистрирован")


# class UserCreateView(FormView):
    
#     form_class = SignUpForm
#     success_url = reverse_lazy('login')
#     template_name = "register.html"

#     def form_valid(self, form):
#         form.save()
#         return super(UserCreateView, self).form_valid(form)


class UserLoginView(SuccessMessageMixin, LoginView):
    
    model = User
    form_class = LoginForm
    template_name = "login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    success_message = _("Вы залогинены")


class UserLogoutView(LogoutView):
    
    next_page = reverse_lazy('home')
    
    def dispatch(self, request, *args, **kwargs):
        messages.info(self.request, _("Вы разлогинены"))
        return super().dispatch(request, *args, **kwargs)
