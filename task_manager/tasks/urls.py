from django.urls import path
from task_manager.tasks import views

app_name = 'tasks'
urlpatterns = [
    path('', views.ObjectListView.as_view(), name='obj_list'),
    path('create/', views.ObjectCreateView.as_view(**views.common_attr), name='obj_create'),
    path(
        '<int:pk>/update/',
        views.ObjectUpdateView.as_view(**views.common_attr),
        name='obj_update'
    ),
    path('<int:pk>/delete/', views.ObjectDeleteView.as_view(), name='obj_delete'),
    path('<int:pk>/', views.ObjectDetailView.as_view(), name='obj_card'),
]
