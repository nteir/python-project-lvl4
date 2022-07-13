from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import SignUpForm, LoginForm
import task_manager.text_constants as txt
from django.db import models
import task_manager.custom_objects as CO

User = get_user_model()


class HomeView(TemplateView):

    template_name = "index.html"


class UsersView(ListView):

    template_name = "users.html"
    model = User
    context_object_name = 'users'
    ordering = ['id']
    paginate_by = 20


class UserCreateView(SuccessMessageMixin, CreateView):

    model = User
    form_class = SignUpForm
    template_name = "form.html"
    success_url = reverse_lazy('login')
    success_message = txt.SIGNUP_SUCSESS
    title_text = txt.SIGNUP_TITLE
    btn_text = txt.SIGNUP_BTN

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title_text
        context['button_text'] = self.btn_text
        return context


class UserUpdateView(CO.CustomEditView, UserPassesTestMixin, UpdateView):

    model = User
    template_name = "form.html"
    form_class = SignUpForm
    success_url = reverse_lazy('users')
    redirect_url = reverse_lazy('users')
    success_message = txt.UPDATE_USER_SUCSESS
    error_message = txt.UPDATE_USER_FAIL
    title_text = txt.UPDATE_USER_TITLE
    btn_text = txt.UPDATE_BTN

    def test_func(self):
        return self.request.user == self.get_object()


class UserDeleteView(CO.CustomEditView, UserPassesTestMixin, DeleteView):

    model = User
    template_name = "delete.html"
    success_url = reverse_lazy('users')
    redirect_url = reverse_lazy('users')
    success_message = txt.DELETE_USER_SUCSESS
    error_message = txt.DELETE_USER_FAIL
    title_text = txt.DELETE_USER_TITLE
    btn_text = txt.DELETE_BTN

    def test_func(self):
        return self.request.user == self.get_object()

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except models.ProtectedError:
            from django.shortcuts import HttpResponseRedirect
            self.error_message = txt.USER_IN_USE
            self.redirect_url = reverse_lazy('users')
            messages.error(self.request, self.error_message)
            return HttpResponseRedirect(self.redirect_url)


class UserLoginView(SuccessMessageMixin, LoginView):

    model = User
    form_class = LoginForm
    template_name = "login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    success_message = txt.LOGIN_SUCSESS


class UserLogoutView(LogoutView):

    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        messages.info(self.request, txt.LOGOUT_SUCSESS)
        return super().dispatch(request, *args, **kwargs)
