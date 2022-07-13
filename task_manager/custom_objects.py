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


class CustomEditView(
    SuccessMessageMixin,
    LoginRequiredMixin,
    FailedAccessMixin,
):

    title_text = ""
    btn_text = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title_text
        context['button_text'] = self.btn_text
        return context
