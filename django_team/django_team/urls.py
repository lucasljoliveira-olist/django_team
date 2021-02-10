from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .team.views import TeamViewSet
from .responsability.views import ResponsabilityViewSet


router = routers.DefaultRouter()
router.register(r'team', TeamViewSet, basename = 'team')
router.register(r'responsability', ResponsabilityViewSet, basename = 'responsability')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]
