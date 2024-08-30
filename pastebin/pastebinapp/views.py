from rest_framework import viewsets

from .models import PasteBin
from .serializers import PasteBinSerializer

class PastebinViewset(viewsets.ModelViewSet):
    serializer_class = PasteBinSerializer
    queryset = PasteBin.objects.all()
    lookup_field = 'hash_code'
