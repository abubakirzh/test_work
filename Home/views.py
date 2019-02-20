from django.shortcuts import render, get_object_or_404, redirect
from Home.models import Snippet
from Home.serializers import SnippetSerializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


def show_homes(request):
    get_homes = Snippet.objects.all()

    return render(request, 'index.html', {'get_homes': get_homes})


def home_detail(request, post_id):
    get_home_detail = get_object_or_404(Snippet, pk=post_id)

    return render(request, 'home_detail.html', {"get_home_detail": get_home_detail})


def search(request):
    if request.method == "POST":
        search_start = request.POST['search']
        search_complete = Snippet.objects.filter(home_title__contains=search_start)
        return render(request, 'index.html', {'search_complete': search_complete,
                                              'search_found': len(search_complete)})

    return redirect('/')