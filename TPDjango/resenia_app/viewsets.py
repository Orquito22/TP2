from rest_framework.viewsets import ModelViewSet
from .models import Resenia
from .serializers import ReseniaSerializer

class ReseniaViewSet(ModelViewSet):
    queryset = Resenia.objects.all()
    serializer_class = ReseniaSerializer