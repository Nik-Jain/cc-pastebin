from rest_framework import viewsets, exceptions
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from datetime import datetime

from .models import PasteBin
from .serializers import PasteBinSerializer
from utils import check_password

class PastebinViewset(viewsets.ModelViewSet):
    serializer_class = PasteBinSerializer
    queryset = PasteBin.objects.all()
    lookup_field = 'hash_code'

    def get_queryset(self):
        paste_exposure = self.request.query_params.get('unlisted')
        if paste_exposure and paste_exposure == 'true':
            return self.queryset.filter(paste_exposure='public')

        return super().get_queryset()
    
    def create(self, request, *args, **kwargs):
        if request.data.get('is_password_protected'):
            data = request.data.copy()
            serializer = PasteBinSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return super().create(request, *args, **kwargs)
    
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
        if datetime.now().astimezone() > record.expire_at:
            record.delete()
            raise NotFound()
        
        if record.is_password_protected:
            if request.data:
                if not check_password(request.data.get('password'), record.password_hash):
                    raise exceptions.AuthenticationFailed()  
            else:
                raise exceptions.NotAcceptable('"Password": "Provide password to access password protected pastes."')
        record.hit_count += 1
        record.save()
        return super().retrieve(request, *args, **kwargs)
