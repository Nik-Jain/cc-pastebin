from rest_framework import serializers
from datetime import datetime, timedelta

from .models import PasteBin
from.helpers import get_expriration_time
from utils import generate_crc32

class PasteBinSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        hash_code = generate_crc32(validated_data.get('input_text', ''))
        validated_data['hash_code'] = hash_code
        paste_expiration = validated_data['paste_expiration']
        validated_data['expire_at'] = get_expriration_time(paste_expiration)
        if not validated_data.get('title'):
            validated_data['title'] = validated_data.get('input_text', '')[:60]
        return super().create(validated_data)
    
    class Meta:
        model =  PasteBin
        fields = '__all__'
        read_only_fields = ['hash_code', 'expire_at', 'hit_count']
