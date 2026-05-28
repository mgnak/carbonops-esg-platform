from django.urls import path
from .views import approve_record, flag_record, lock_record

urlpatterns = [
    path('<int:pk>/approve/', approve_record),
    path('<int:pk>/flag/', flag_record),
    path('<int:pk>/lock/', lock_record),
]