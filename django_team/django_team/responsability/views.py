from rest_framework import viewsets
from .serializers import ResponsabilitySerializer
from .models import Responsability

class ResponsabilityViewSet(viewsets.ModelViewSet):
    queryset = Responsability.objects.all().order_by('name')
    serializer_class = ResponsabilitySerializer
