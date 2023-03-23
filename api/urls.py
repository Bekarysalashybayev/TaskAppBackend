from rest_framework.routers import DefaultRouter, SimpleRouter

from api import views
from django.urls.conf import path, include

router = DefaultRouter()

router.register("task", views.ItemModelViewSet, basename="task")

urlpatterns = [
    path('', include(router.urls))
]
