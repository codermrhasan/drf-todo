from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from todos import views


urlpatterns = [
    path('', views.api_root),
    path('todos/', views.TodoList.as_view(), name='todo-list'),
    path('todos/<int:pk>/', views.TodoDetail.as_view(), name='todo-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail')
]

urlpatterns += [
    path('', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
