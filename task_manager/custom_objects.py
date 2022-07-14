from django.contrib.auth.mixins import AccessMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect


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
    title_text = ""
    btn_text = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title_text
        context['button_text'] = self.btn_text
        return context


def get_path_arguments(module, obj_name):
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
        {'name': f'{obj_name}_list', },
        {'name': f'{obj_name}_create', },
        {'name': f'{obj_name}_update', },
        {'name': f'{obj_name}_delete', },
    ]
    return list(zip(args, kwargs))
