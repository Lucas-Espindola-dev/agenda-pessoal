from rest_framework import serializers
from agenda.models import Compromissos


class CompromissoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compromissos
        fields = '__all__'
