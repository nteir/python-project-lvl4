from django.urls import path
from task_manager.tasks import views
from task_manager.custom_objects import get_path_arguments

arguments = get_path_arguments(views, 'task')
urlpatterns = [path(*a, **k) for a, k in arguments]
detail_path = path('<int:pk>/', views.ObjectDetailView.as_view(), name='task_card')
urlpatterns.append(detail_path)
