from rest_framework import viewsets
from agenda.models import Compromissos


class AgendaViewset(viewsets.ModelViewSet):
    queryset = Compromissos.objects.all()
    serializer_class = None
