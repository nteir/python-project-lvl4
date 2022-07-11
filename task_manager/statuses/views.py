# from django.shortcuts import render
from .models import TaskStatus
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from .forms import StatusCreateForm
import task_manager.statuses.text_constants as txt
from task_manager.views import get_form_context


# Create your views here.
class StatusListView(LoginRequiredMixin, ListView):
    
    model = TaskStatus
    template_name = "statuses/statuses.html"
    context_object_name = 'statuses'
    ordering = ['id']
    redirect_url = reverse_lazy('login')
    error_message = txt.CREATE_STATUS_FAIL

    def handle_no_permission(self):
        messages.error(self.request, self.error_message)
        return redirect(self.redirect_url)


class StatusCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    
    model = TaskStatus
    form_class = StatusCreateForm
    template_name = "form.html"
    success_url = reverse_lazy('status_list')
    redirect_url = reverse_lazy('login')
    success_message = txt.CREATE_STATUS_SUCSESS
    error_message = txt.CREATE_STATUS_FAIL

    def handle_no_permission(self):
        messages.error(self.request, self.error_message)
        return redirect(self.redirect_url)
    
    def get_context_data(self, **kwargs):
        return get_form_context(
            txt.CREATE_TITLE,
            txt.CREATE_BTN, self,
            **kwargs
        )
