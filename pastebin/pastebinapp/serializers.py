from rest_framework import serializers
from datetime import datetime, timedelta

from .models import PasteBin
from.helpers import get_expriration_time
from utils import generate_crc32, generate_hash_password

class PasteBinSerializer(serializers.ModelSerializer):

    password = serializers.CharField(required=False)

    def create(self, validated_data):
        # Generate a hash code based on the input text
        hash_code = generate_crc32(validated_data.get('input_text', ''))
        validated_data['hash_code'] = hash_code
        
        # Set the expiration time based on paste_expiration
        paste_expiration = validated_data['paste_expiration']
        validated_data['expire_at'] = get_expriration_time(paste_expiration)
        
        # Set a default title if it's not provided
        if not validated_data.get('title'):
            validated_data['title'] = validated_data.get('input_text', '')[:60]
        
        # Handle password protection
        if validated_data.get('is_password_protected'):
            password = validated_data.pop('password', None)
            if password:
                password_hash = generate_hash_password(password)
                validated_data['password_hash'] = password_hash
            else:
                raise serializers.ValidationError('password: Password is required when is_password_protected is True.')
            
        return super().create(validated_data)
    
    class Meta:
        model =  PasteBin
        # fields = '__all__'
        read_only_fields = ['hash_code', 'expire_at', 'hit_count']
        exclude = ['password_hash',]
