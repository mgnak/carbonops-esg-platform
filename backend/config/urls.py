from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),

    path(
        'api/emissions/',
        include('apps.emissions.urls')
    ),

    path(
        'api/review/',
        include('apps.review.urls')
    ),

    path(
        'api/ingestion/',
        include('apps.ingestion.urls')
    ),
]