from rest_framework import serializers
from Home.models import *


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = (
            'title',
            'type',
            'price',
            'description',
            'location',
            'contacts'
        )
