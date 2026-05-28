from rest_framework.generics import ListAPIView
from .models import EmissionRecord
from .serializers import EmissionRecordSerializer


class EmissionListView(ListAPIView):
    queryset = EmissionRecord.objects.all().order_by('-created_at')
    serializer_class = EmissionRecordSerializer