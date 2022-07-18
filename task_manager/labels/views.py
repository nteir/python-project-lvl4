from .models import Label
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
    'success_url': reverse_lazy('labels:obj_list'),
    'redirect_url': reverse_lazy('login'),
    'error_message': txt.NOT_LOGGED_IN,
}


# Create your views here.
class ObjectListView(CO.CustomListView):

    model = Label
    app_name = 'labels'
    title = txt.LABEL_LIST_TITLE
    new_obj_text = txt.LABEL_LIST_NEW


class ObjectCreateView(CO.CustomEditView, CreateView):

    success_message = txt.CREATE_LABEL_SUCSESS
    title_text = txt.CREATE_LABEL_TITLE
    btn_text = txt.CREATE_BTN


class ObjectUpdateView(CO.CustomEditView, UpdateView):

    success_message = txt.UPDATE_LABEL_SUCSESS
    title_text = txt.UPDATE_LABEL_TITLE
    btn_text = txt.UPDATE_BTN


class ObjectDeleteView(CO.CustomEditView, DeleteView):

    model = Label
    template_name = "delete.html"
    success_url = reverse_lazy('labels:obj_list')
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
            self.redirect_url = reverse_lazy('labels:obj_list')
            messages.error(self.request, self.error_message)
            return HttpResponseRedirect(self.redirect_url)
