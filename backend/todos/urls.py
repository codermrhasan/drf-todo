from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todos import views

router = DefaultRouter()
router.register(r'snippets', views.TodoViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls')),
]
