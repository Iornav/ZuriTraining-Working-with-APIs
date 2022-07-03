
from rest_framework import serializers
from links.models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'
        read_only_fields = ('author', 'created_date')
        extra_kwargs = {
            'identifier': {'required': False},
        }