from Home.models import Home
from Home.serializers import HomeSerializer
from rest_framework import generics


class HomeList(generics.ListCreateAPIView):
    queryset = Home.objects.order_by('price')
    # queryset_high_to_low = Home.objects.order_by('price')
    # queryset_flat_only = Home.objects.order_by('type')
    serializer_class = HomeSerializer


class HomeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
