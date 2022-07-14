from django.urls import path
from task_manager.labels import views

urlpatterns = [
    path('', views.LabelListView.as_view(), name='label_list'),
    path(
        'create/',
        views.LabelCreateView.as_view(**views.common_attr),
        name='label_create'
    ),
    path(
        '<int:pk>/update/',
        views.LabelUpdateView.as_view(**views.common_attr),
        name='label_update'
    ),
    path(
        '<int:pk>/delete/',
        views.LabelDeleteView.as_view(),
        name='label_delete'
    ),
]
