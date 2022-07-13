from django.urls import path
from task_manager.tasks import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path(
        '<int:pk>/',
        views.TaskDetailView.as_view(),
        name='task_card'
    ),
    path(
        'create/',
        views.TaskCreateView.as_view(**views.common_attr),
        name='task_create'
    ),
    path(
        '<int:pk>/update/',
        views.TaskUpdateView.as_view(**views.common_attr),
        name='task_update'
    ),
    path(
        '<int:pk>/delete/',
        views.TaskDeleteView.as_view(),
        name='task_delete'
    ),
]
