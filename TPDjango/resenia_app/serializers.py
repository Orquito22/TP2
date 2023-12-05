from rest_framework.serializers import ModelSerializer
from .models import Resenia

class ReseniaSerializer(ModelSerializer):
    class Meta:
        model = Resenia
        fields = "__all__"