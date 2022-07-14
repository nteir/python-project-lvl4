from .models import Label
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import LabelCreateForm
import task_manager.text_constants as txt
from django.db import models
import task_manager.custom_objects as CO


# Common attributes for Create and Update Views
common_attr = {
    'model': Label,
    'form_class': LabelCreateForm,
    'template_name': "form.html",
    'success_url': reverse_lazy('label_list'),
    'redirect_url': reverse_lazy('login'),
    'error_message': txt.NOT_LOGGED_IN,
}


# Create your views here.
class LabelListView(CO.FailedAccessMixin, LoginRequiredMixin, ListView):

    model = Label
    template_name = "labels/labels.html"
    context_object_name = 'labels'
    ordering = ['id']
    redirect_url = reverse_lazy('login')
    error_message = txt.NOT_LOGGED_IN


class LabelCreateView(CO.CustomEditView, CreateView):

    success_message = txt.CREATE_LABEL_SUCSESS
    title_text = txt.CREATE_LABEL_TITLE
    btn_text = txt.CREATE_BTN


class LabelUpdateView(CO.CustomEditView, UpdateView):

    success_message = txt.UPDATE_LABEL_SUCSESS
    title_text = txt.UPDATE_LABEL_TITLE
    btn_text = txt.UPDATE_BTN


class LabelDeleteView(CO.CustomEditView, DeleteView):

    model = Label
    template_name = "delete.html"
    success_url = reverse_lazy('label_list')
    redirect_url = reverse_lazy('login')
    success_message = txt.DELETE_LABEL_SUCSESS
    error_message = txt.NOT_LOGGED_IN
    title_text = txt.DELETE_LABEL_TITLE
    btn_text = txt.DELETE_BTN

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except models.ProtectedError:
            from django.shortcuts import HttpResponseRedirect
            from django.contrib import messages
            self.error_message = txt.LABEL_IN_USE
            self.redirect_url = reverse_lazy('label_list')
            messages.error(self.request, self.error_message)
            return HttpResponseRedirect(self.redirect_url)