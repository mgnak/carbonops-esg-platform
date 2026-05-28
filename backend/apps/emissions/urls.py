from django.urls import path
from .views import EmissionListView

urlpatterns = [
    path('', EmissionListView.as_view()),
]