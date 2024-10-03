from django.urls import path, include
from rest_framework import routers
from ConSens import views

router=routers.DefaultRouter()
router.register(r"registros", views.RegistrosViewSet)

urlpatterns = [
    path(" ", include(router.urls)),
]
