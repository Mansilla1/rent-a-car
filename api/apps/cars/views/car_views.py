from django.db.models import (
    Count,
    F,
    Prefetch,
)
from rest_framework.generics import ListAPIView

from apps.cars.models import (
    Car,
    CarAvailability,
)
from apps.cars.serializers import CarSerializer


class CarList(ListAPIView):

    serializer_class = CarSerializer

    queryset = Car.objects.select_related(
        'model',
        'model__brand',
    ).prefetch_related(
        Prefetch(
            'car_availibility',
            queryset=CarAvailability.objects.filter(available=True),
            to_attr='availability',
        ),
    ).annotate(
        brand_name=F('model__brand__name'),
        model_name=F('model__name'),
    )
