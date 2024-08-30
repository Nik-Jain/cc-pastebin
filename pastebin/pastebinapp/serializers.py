from rest_framework import serializers

from .models import PasteBin
from utils import generate_crc32

class PasteBinSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        hash_code = generate_crc32(validated_data.get('input_text', ''))
        validated_data['hash_code'] = hash_code
        return super().create(validated_data)
    
    class Meta:
        model =  PasteBin
        fields = '__all__'
        read_only_fields = ['hash_code']
