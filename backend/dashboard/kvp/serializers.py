from rest_framework import serializers

from .models import Kvp

class KvpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kvp
        fields = ('id', 'key', 'value')