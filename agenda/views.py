from rest_framework import viewsets
from agenda.models import Compromissos
from agenda.serializer import CompromissoSerializer


class AgendaViewset(viewsets.ModelViewSet):
    queryset = Compromissos.objects.all()
    serializer_class = CompromissoSerializer
