from rest_framework import serializers
from Home.models import *

#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Snippet
#         fields = ('home_type', 'home_price', 'home_description', 'home_location', 'home_contacts')


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('home_type', 'home_price', 'home_description', 'home_location', 'home_contacts')