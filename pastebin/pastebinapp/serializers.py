from rest_framework import serializers

from .models import Bin
from utils import generate_crc32

class BinSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        hash_code = generate_crc32(validated_data.get('input_text', ''))
        validated_data['hash_code'] = hash_code
        return super().create(validated_data)
    
    class Meta:
        model =  Bin
        fields = '__all__'
        read_only_fields = ['hash_code']
