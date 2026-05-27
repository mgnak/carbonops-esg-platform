from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include


def home(request):
    return JsonResponse({
        "message": "Breathe ESG Backend Running"
    })


urlpatterns = [

    path('', home),

    path('admin/', admin.site.urls),

    path(
        'api/ingestion/',
        include('apps.ingestion.urls')
    ),

    path(
        'api/emissions/',
        include('apps.emissions.urls')
    ),

    path(
        'api/review/',
        include('apps.review.urls')
    ),
]