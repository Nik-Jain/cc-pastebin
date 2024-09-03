from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from datetime import datetime

from .models import PasteBin
from .serializers import PasteBinSerializer

class PastebinViewset(viewsets.ModelViewSet):
    serializer_class = PasteBinSerializer
    queryset = PasteBin.objects.all()
    lookup_field = 'hash_code'

    def retrieve(self, request, *args, **kwargs):
        
        hash_code = kwargs['hash_code']
        
        try:
            record = PasteBin.objects.get(hash_code=hash_code)
        except PasteBin.DoesNotExist:
            raise NotFound()
        
        # Burst After Read
        if record.paste_expiration == "BU" and record.hit_count > 0:
            record.delete()
            raise NotFound()
        
        # Passive Expiration
        if datetime.now() > record.expire_at:
            record.delete()
            raise NotFound()
        
        record.hit_count += 1
        record.save()
        return super().retrieve(request, *args, **kwargs)
