from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import gettext


class MainView(TemplateView):
    template_name = "index.html"


# def index(request):
#     return render(request, 'index.html', context={})
