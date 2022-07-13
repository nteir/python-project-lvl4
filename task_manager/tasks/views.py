from .models import Task
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import TaskCreateForm
import task_manager.text_constants as txt
import task_manager.custom_objects as CO

# Common attributes for Create and Update Views
common_attr = {
    'model': Task,
    'form_class': TaskCreateForm,
    'template_name': "form.html",
    'success_url': reverse_lazy('task_list'),
    'redirect_url': reverse_lazy('login'),
    'error_message': txt.NOT_LOGGED_IN,
}


# Create your views here.
class TaskListView(CO.FailedAccessMixin, LoginRequiredMixin, ListView):

    model = Task
    template_name = "tasks/tasks.html"
    context_object_name = 'tasks'
    ordering = ['id']
    redirect_url = reverse_lazy('login')
    error_message = txt.NOT_LOGGED_IN


class TaskDetailView(LoginRequiredMixin, DetailView):

    model = Task
    template_name = "tasks/task_card.html"
    context_object_name = 'task'
    redirect_url = reverse_lazy('login')
    error_message = txt.NOT_LOGGED_IN


class TaskCreateView(CO.CustomEditView, CreateView):

    success_message = txt.CREATE_TASK_SUCSESS
    title_text = txt.CREATE_TASK_TITLE
    btn_text = txt.CREATE_BTN

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)


class TaskUpdateView(CO.CustomEditView, UpdateView):

    success_message = txt.UPDATE_TASK_SUCSESS
    title_text = txt.UPDATE_TASK_TITLE
    btn_text = txt.UPDATE_BTN


class TaskDeleteView(CO.CustomEditView, UserPassesTestMixin, DeleteView):

    model = Task
    template_name = "delete.html"
    success_url = reverse_lazy('task_list')
    redirect_url = reverse_lazy('task_list')
    success_message = txt.DELETE_TASK_SUCSESS
    error_message = txt.DELETE_TASK_FAIL
    title_text = txt.DELETE_TASK_TITLE
    btn_text = txt.DELETE_BTN

    def test_func(self):
        return self.request.user == self.get_object().author
