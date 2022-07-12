# from django.contrib.auth.models import User
# from task_manager.models import User
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .custom_objects import FailedAccessMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import SignUpForm, LoginForm
import task_manager.text_constants as txt

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

    def get_context_data(self, **kwargs):
        return get_form_context(
            txt.SIGNUP_TITLE,
            txt.SIGNUP_BTN, self,
            **kwargs
        )


class UserUpdateView(
    SuccessMessageMixin,
    LoginRequiredMixin,
    UserPassesTestMixin,
    FailedAccessMixin,
    UpdateView
):

    model = User
    template_name = "form.html"
    form_class = SignUpForm
    success_url = reverse_lazy('users')
    redirect_url = reverse_lazy('users')
    success_message = txt.UPDATE_USER_SUCSESS
    error_message = txt.UPDATE_USER_FAIL

    def test_func(self):
        return self.request.user == self.get_object()

    def get_context_data(self, **kwargs):
        return get_form_context(
            txt.UPDATE_TITLE,
            txt.UPDATE_BTN, self,
            **kwargs
        )


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
    success_message = txt.DELETE_USER_SUCSESS
    error_message = txt.DELETE_USER_FAIL

    def test_func(self):
        return self.request.user == self.get_object()

    def get_context_data(self, **kwargs):
        return get_form_context(
            txt.DELETE_TITLE,
            txt.DELETE_BTN, self,
            **kwargs
        )


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


def get_form_context(title, btn, obj, **kwargs):
    context = super(obj.__class__, obj).get_context_data(**kwargs)
    context['title'] = title
    context['button_text'] = btn
    return context
