from .models import Label
from django.views.generic.edit import DeleteView
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

list_view_attr = {
    'model': Label,
    'app_name': 'labels',
    'title': txt.LABEL_LIST_TITLE,
    'new_obj_text': txt.LABEL_LIST_NEW,
}

create_view_attr = {
    'success_message': txt.CREATE_LABEL_SUCSESS,
    'title_text': txt.CREATE_LABEL_TITLE,
    'btn_text': txt.CREATE_BTN,
}
create_view_attr.update(common_attr)

update_view_attr = {
    'success_message': txt.UPDATE_LABEL_SUCSESS,
    'title_text': txt.UPDATE_LABEL_TITLE,
    'btn_text': txt.UPDATE_BTN,
}
update_view_attr.update(common_attr)


# Create your views here.
# Re-using the List, Create and Update views from statuses


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
