from django import forms
from .models import TaskStatus


class StatusCreateForm(forms.ModelForm):
    class Meta:
        model = TaskStatus
        fields = [
            'name',
        ]
