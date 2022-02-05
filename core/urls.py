from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from pull_requests.views import get_index, make_request


urlpatterns = [
    path('', get_index),
    path('pulls', make_request, name='github_url'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_URL)