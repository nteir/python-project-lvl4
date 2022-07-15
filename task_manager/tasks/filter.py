import django_filters
from django import forms
from task_manager.labels.models import Label
from .models import Task
import task_manager.text_constants as txt


class TaskFilter(django_filters.FilterSet):

    label_set = Label.objects.values_list('id', 'name').all()
    labels = django_filters.filters.ChoiceFilter(choices=label_set)

    user_tasks = django_filters.filters.BooleanFilter(
        label=txt.FILTER_MY_TASKS,
        widget=forms.CheckboxInput(),
        method='get_uesr_tasks'
    )

    def get_uesr_tasks(self, queryset, name, value):
        if value:
            author = getattr(self.request, "user", None)
            queryset = queryset.filter(author=author)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
