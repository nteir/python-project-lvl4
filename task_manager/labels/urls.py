from django.urls import path
from task_manager.labels import views
from task_manager.statuses import views as statuses_views

app_name = 'labels'

urlpatterns = [
    path('', statuses_views.ObjectListView.as_view(**views.list_view_attr), name='obj_list'),
    path(
        'create/',
        statuses_views.ObjectCreateView.as_view(**views.create_view_attr),
        name='obj_create'
    ),
    path(
        '<int:pk>/update/',
        statuses_views.ObjectUpdateView.as_view(**views.update_view_attr),
        name='obj_update'
    ),
    path(
        '<int:pk>/delete/',
        statuses_views.ObjectDeleteView.as_view(**views.delete_view_attr),
        name='obj_delete'
    ),
]
