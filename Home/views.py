from django.shortcuts import render, get_object_or_404, redirect
from Home.models import Home
from Home.serializers import HomeSerializer
from rest_framework import generics


class HomeList(generics.ListCreateAPIView):
    queryset = Home.objects.order_by('-price')
    # queryset_low_to_high = Home.objects.order_by('price')
    # queryset_flat_only = Home.objects.order_by('type')

    serializer_class = HomeSerializer


class HomeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


def show_homes(request):
    get_homes = Home.objects.all()

    return render(request, 'index.html', {'get_homes': get_homes})


def home_detail(request, post_id):
    get_home_detail = get_object_or_404(Home, pk=post_id)

    return render(request, 'home_detail.html', {"get_home_detail": get_home_detail})


def search(request):
    if request.method == "POST":
        search_start = request.POST['search']
        search_complete = Home.objects.filter(home_title__contains=search_start)
        return render(request, 'index.html', {'search_complete': search_complete,
                                              'search_found': len(search_complete)})

    return redirect('/')
