from rest_framework import serializers
from .models import *

class CustomSerializer(serializers.ModelSerializer):

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(CustomSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields

class TransactionSerializer(CustomSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        extra_fields= ['summary']

class ItemSerializer(CustomSerializer):
    transactions = TransactionSerializer(read_only=True,many=True)
    level_name = serializers.SlugRelatedField(source='level',read_only=True, slug_field='level')
    
    class Meta:
        model = Item
        fields = '__all__'
        extra_fields= ['summary','level_name','transactions']
