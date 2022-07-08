# from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, AccessMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from .custom_objects import FailedAccessMixin
from django.contrib.messages.views import SuccessMessageMixin



class HomeView(TemplateView):
    
    template_name = "index.html"


class UsersView(ListView):
    
    template_name = "users.html"
    model = User
    context_object_name = 'users'
    ordering = ['id']
    paginate_by = 10


class UserCreateView(SuccessMessageMixin, CreateView):

    model = User
    form_class = SignUpForm
    template_name = "register.html"
    success_url = reverse_lazy('login')
    success_message = _("Пользователь успешно зарегистрирован")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Sign up')
        context['button_text'] = _('Sign up')
        return context


# class UserCreateView(FormView):
    
#     form_class = SignUpForm
#     success_url = reverse_lazy('login')
#     template_name = "register.html"

#     def form_valid(self, form):
#         form.save()
#         return super(UserCreateView, self).form_valid(form)


class UserUpdateView(
    SuccessMessageMixin,
    LoginRequiredMixin,
    UserPassesTestMixin,
    FailedAccessMixin,
    UpdateView
    ):

    model = User
    template_name = "register.html"
    form_class = SignUpForm
    success_url = reverse_lazy('users')
    redirect_url = reverse_lazy('users')
    success_message = _("Пользователь успешно изменён")
    error_message = _("У вас нет прав для изменения другого пользователя.")

    def test_func(self):
        return self.request.user == self.get_object()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Update user')
        context['button_text'] = _('Update')
        return context


class UserDeleteView(
    SuccessMessageMixin,
    LoginRequiredMixin,
    UserPassesTestMixin,
    FailedAccessMixin,
    DeleteView
    ):
    
    model = User
    template_name = "delete.html"
    success_url = reverse_lazy('users')
    redirect_url = reverse_lazy('users')
    success_message = _("Пользователь успешно удалён")
    error_message = _("У вас нет прав для изменения другого пользователя.")

    def test_func(self):
        return self.request.user == self.get_object()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Удаление пользователя')
        context['button_text'] = _('Да, удалить')
        return context


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
