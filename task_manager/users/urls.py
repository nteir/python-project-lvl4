from django.urls import path
from task_manager.users import views


app_name = 'users'
urlpatterns = [
    path('', views.UsersView.as_view(), name='users'),
    path('users/create/', views.UserCreateView.as_view(), name='signup'),
    path(
        'users/<int:pk>/update/',
        views.UserUpdateView.as_view(),
        name='update'
    ),
    path(
        'users/<int:pk>/delete/',
        views.UserDeleteView.as_view(),
        name='delete'
    ),
]
