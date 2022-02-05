from django.urls import path
from plapp.views import get_index, make_request


urlpatterns = [
    path('', get_index),
    path('pulls', make_request, name='github_url'),
]