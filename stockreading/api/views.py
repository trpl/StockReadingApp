from rest_framework import (
    serializers,
    mixins,
    viewsets
)

from stockreading.models import StockReading

class StockReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StockReading
        fields = ["id", 'reference_id', 'expiry_date', 'created_on']
        read_only_fields = ("id", "created_on")


class StockReadingViewSet(mixins.CreateModelMixin,
							mixins.ListModelMixin,
							mixins.RetrieveModelMixin,
							viewsets.GenericViewSet):
    queryset = StockReading.objects.all().order_by('created_on')
    serializer_class = StockReadingSerializer
