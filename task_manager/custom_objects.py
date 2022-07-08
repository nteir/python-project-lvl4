from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages
from django.shortcuts import redirect


class FailedAccessMixin(AccessMixin):
    redirect_url = ""
    error_message = ""

    def handle_no_permission(self):
        messages.error(self.request, self.error_message)
        return redirect(self.redirect_url)
