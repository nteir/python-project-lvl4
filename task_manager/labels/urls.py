from django.urls import path
from task_manager.labels import views
from task_manager.custom_objects import get_path_arguments

arguments = get_path_arguments(views, 'label')
urlpatterns = [path(*a, **k) for a, k in arguments]
