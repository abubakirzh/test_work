from rest_framework import serializers
from Home.models import *

#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Snippet
#         fields = ('home_type', 'home_price', 'home_description', 'home_location', 'home_contacts')


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ('title', 'type', 'price', 'description', 'location', 'contacts')
