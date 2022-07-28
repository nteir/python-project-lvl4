from django.contrib.auth.mixins import AccessMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse_lazy
import task_manager.text_constants as txt


class FailedAccessMixin(AccessMixin):
    """
    Overrides handle_no_permission to redirect
    instead of sending err code response,
    and sets an error flash message.
    """
    redirect_url = ""
    error_message = ""

    def handle_no_permission(self):
        messages.error(self.request, self.error_message)
        return redirect(self.redirect_url)


class CustomEditView(SuccessMessageMixin, LoginRequiredMixin, FailedAccessMixin):
    """
    Overrides get_context_data adding
    title and button text attributes to use
    in reusable form pages.
    """
    title_text = ''
    btn_text = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title_text
        context['button_text'] = self.btn_text
        return context


class CustomListView(FailedAccessMixin, LoginRequiredMixin, ListView):
    """
    Common properties for statuses and labels
    list views.
    """
    ordering = ['id']
    redirect_url = reverse_lazy('login')
    error_message = txt.NOT_LOGGED_IN
    template_name = 'list.html'
    context_object_name = 'objects'
    app_name = ''
    title = ''
    new_obj_text = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = self.app_name
        context['title'] = self.title
        context['new_obj_text'] = self.new_obj_text
        return context


class CustomDeleteView(CustomEditView, DeleteView):

    template_name = "delete.html"
    redirect_url = reverse_lazy('login')
    error_message = txt.NOT_LOGGED_IN
    btn_text = txt.DELETE_BTN
    in_use_text = ''

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except models.ProtectedError:
            self.error_message = self.in_use_text
            self.redirect_url = self.success_url
            messages.error(self.request, self.error_message)
            return HttpResponseRedirect(self.redirect_url)


def get_path_arguments(module):
    """
    Arguments to generate urlpatterns for
    List, Create, Update, Delete views,
    common for statuses, labels and tasks.
    """
    args = [
        [
            '',
            module.ObjectListView.as_view(),
        ],
        [
            'create/',
            module.ObjectCreateView.as_view(**module.common_attr),
        ],
        [
            '<int:pk>/update/',
            module.ObjectUpdateView.as_view(**module.common_attr),
        ],
        [
            '<int:pk>/delete/',
            module.ObjectDeleteView.as_view(),
        ],
    ]
    kwargs = [
        {'name': 'obj_list', },
        {'name': 'obj_create', },
        {'name': 'obj_update', },
        {'name': 'obj_delete', },
    ]
    return list(zip(args, kwargs))
