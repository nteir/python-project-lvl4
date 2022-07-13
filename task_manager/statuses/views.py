from .models import TaskStatus
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.custom_objects import FailedAccessMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import StatusCreateForm
import task_manager.statuses.text_constants as txt
from task_manager.views import get_form_context
from django.db import models

# Common attributes for Create and Update Views
common_attr = {
    'model': TaskStatus,
    'form_class': StatusCreateForm,
    'template_name': "form.html",
    'success_url': reverse_lazy('status_list'),
    'redirect_url': reverse_lazy('login'),
    'error_message': txt.NOT_LOGGED_IN,
}


# Create your views here.
class StatusListView(FailedAccessMixin, LoginRequiredMixin, ListView):

    model = TaskStatus
    template_name = "statuses/statuses.html"
    context_object_name = 'statuses'
    ordering = ['id']
    redirect_url = reverse_lazy('login')
    error_message = txt.NOT_LOGGED_IN


class StatusCreateView(
    SuccessMessageMixin,
    FailedAccessMixin,
    LoginRequiredMixin,
    CreateView
):

    success_message = txt.CREATE_STATUS_SUCSESS

    def get_context_data(self, **kwargs):
        return get_form_context(
            txt.CREATE_TITLE,
            txt.CREATE_BTN, self,
            **kwargs
        )


class StatusUpdateView(
    SuccessMessageMixin,
    LoginRequiredMixin,
    FailedAccessMixin,
    UpdateView
):

    success_message = txt.UPDATE_STATUS_SUCSESS

    def get_context_data(self, **kwargs):
        return get_form_context(
            txt.UPDATE_TITLE,
            txt.UPDATE_BTN, self,
            **kwargs
        )


class StatusDeleteView(
    SuccessMessageMixin,
    LoginRequiredMixin,
    FailedAccessMixin,
    DeleteView
):
    model = TaskStatus
    template_name = "delete.html"
    success_url = reverse_lazy('status_list')
    redirect_url = reverse_lazy('login')
    success_message = txt.DELETE_STATUS_SUCSESS
    error_message = txt.NOT_LOGGED_IN

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except models.ProtectedError:
            from django.shortcuts import HttpResponseRedirect
            from django.contrib import messages
            self.error_message = txt.STATUS_IN_USE
            self.redirect_url = reverse_lazy('status_list')
            messages.error(self.request, self.error_message)
            return HttpResponseRedirect(self.redirect_url)

    def get_context_data(self, **kwargs):
        return get_form_context(
            txt.DELETE_TITLE,
            txt.DELETE_BTN, self,
            **kwargs
        )
