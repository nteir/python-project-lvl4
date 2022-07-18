from django.urls import path
from task_manager.tasks import views
from task_manager.custom_objects import get_path_arguments

app_name = 'tasks'
arguments = get_path_arguments(views)
urlpatterns = [path(*a, **k) for a, k in arguments]
detail_path = path('<int:pk>/', views.ObjectDetailView.as_view(), name='obj_card')
urlpatterns.append(detail_path)
