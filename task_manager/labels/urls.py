from django.urls import path
from task_manager.labels import views
from task_manager.statuses import views as statuses_views
# from task_manager.custom_objects import get_path_arguments

app_name = 'labels'
# arguments = get_path_arguments(views)
# urlpatterns = [path(*a, **k) for a, k in arguments]

urlpatterns = [
    path('', statuses_views.ObjectListView.as_view(**views.list_view_attr), name='obj_list'),
    path('create/', statuses_views.ObjectCreateView.as_view(**views.create_view_attr), name='obj_create'),
    path('<int:pk>/update/', statuses_views.ObjectUpdateView.as_view(**views.update_view_attr), name='obj_update'),
    path('<int:pk>/delete/', statuses_views.ObjectDeleteView.as_view(**views.delete_view_attr), name='obj_delete'),
]
