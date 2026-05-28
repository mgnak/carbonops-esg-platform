from django.urls import path
from .views import upload_sap_file

urlpatterns = [
    path(
        'sap/upload/',
        upload_sap_file,
        name='upload_sap_file'
    ),
]