from rest_framework import serializers

# TODO: опишите необходимые сериализаторы

from measurement.models import Sensor, Measurement

class SensorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sensor
        fields = ('id', 'name', 'description')
        

class MeasurementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Measurement
        fields = ('id','temperature', 'created_at', 'sensor_id')