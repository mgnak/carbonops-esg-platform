# # from django.urls import path, include
# # from rest_framework.routers import DefaultRouter
# # from .views import CompanyViewSet, DataSourceViewSet, EmissionRecordViewSet

# router = DefaultRouter()
# router.register(r'companies', CompanyViewSet)
# router.register(r'datasources', DataSourceViewSet)
# router.register(r'emission-records', EmissionRecordViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]


# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import EmissionRecordViewSet
from ingestion.views import FileUploadView

router = DefaultRouter()
router.register(r'emission-records', EmissionRecordViewSet, basename='emissionrecord')

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
]