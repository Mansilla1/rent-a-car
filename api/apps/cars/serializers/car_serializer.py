from rest_framework import serializers

from apps.cars.models import (
    Car,
    CarAvailability,
)


class CarAvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = CarAvailability
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField()
    model_name = serializers.CharField()
    availability = CarAvailabilitySerializer(many=True)

    class Meta:
        model = Car
        fields = (
            'brand_name',
            'model_name',
            'doors',
            'high',
            'long',
            'width',
            'weight',
            'diesel',
            'description',
            'availability',
        )
