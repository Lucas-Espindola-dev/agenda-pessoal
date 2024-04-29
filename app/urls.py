from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from agenda.views import AgendaViewset

router = routers.DefaultRouter()
router.register('agenda', AgendaViewset, basename='agenda')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
