from rest_framework import viewsets

from .models import Bin
from .serializers import BinSerializer

class PastebinViewset(viewsets.ModelViewSet):
    serializer_class = BinSerializer
    queryset = Bin.objects.all()
    lookup_field = 'hash_code'
