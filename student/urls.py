from django.urls import path, include
from rest_framework.routers import DefaultRouter
from student.views import TaskViewSet

router = DefaultRouter()

router.register('task', TaskViewSet, basename='task')


urlpatterns = []

urlpatterns += router.urls
