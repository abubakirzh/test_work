from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Home import views

urlpatterns = [
    path('homes/', views.HomeList.as_view()),
    # path('homes/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
