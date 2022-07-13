from .models import Task
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.custom_objects import FailedAccessMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import TaskCreateForm
import task_manager.tasks.text_constants as txt
from task_manager.views import get_form_context


# Create your views here.
class TaskListView(FailedAccessMixin, LoginRequiredMixin, ListView):

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


class TaskCreateView(
    SuccessMessageMixin,
    FailedAccessMixin,
    LoginRequiredMixin,
    CreateView
):

    model = Task
    form_class = TaskCreateForm
    template_name = "form.html"
    success_url = reverse_lazy('task_list')
    redirect_url = reverse_lazy('login')
    error_message = txt.NOT_LOGGED_IN
    success_message = txt.CREATE_TASK_SUCSESS

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super(TaskCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        return get_form_context(
            txt.CREATE_TITLE,
            txt.CREATE_BTN, self,
            **kwargs
        )


class TaskUpdateView(
    SuccessMessageMixin,
    LoginRequiredMixin,
    FailedAccessMixin,
    UpdateView
):
    pass


class TaskDeleteView(
    SuccessMessageMixin,
    LoginRequiredMixin,
    FailedAccessMixin,
    DeleteView
):
    pass
