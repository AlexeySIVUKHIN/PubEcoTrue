from rest_framework import serializers
from rest_framework.utils import json

from appeal.models import *

# class SensorDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SensorDataTable
#         fields = "__all__"


# class SensorDataSerializer(serializers.Serializer):
#     # esp8266id = serializers.CharField()
#     # software_version = serializers.CharField()
#     sensordatavalues = serializers.ListField(
#         child=serializers.DictField(
#             child=serializers.CharField()
#         )
#     )
#
#     def create(self, sensordatavalues):
#         new_data = {}
#         for item in sensordatavalues:
#             if item['value_type'] != 'esp8266id' and item['value_type'] != 'software_version':
#                 new_data[item['value_type']] = item['value']
#         return new_data
from rest_framework import serializers

# class SensorDataSerializer(serializers.Serializer):
#     SDS_P1 = serializers.DecimalField(max_digits=5, decimal_places=2)
#     SDS_P2 = serializers.DecimalField(max_digits=5, decimal_places=2)
#     BME280_temperature = serializers.DecimalField(max_digits=5, decimal_places=2)
#     BME280_pressure = serializers.DecimalField(max_digits=8, decimal_places=2)
#     BME280_humidity = serializers.DecimalField(max_digits=5, decimal_places=2)
#     samples = serializers.IntegerField()
#     min_micro = serializers.IntegerField()
#     max_micro = serializers.IntegerField()
#     interval = serializers.IntegerField()
#     signal = serializers.IntegerField()

class SensorDataSerializer(serializers.ModelSerializer):
    esp8266id = models.PositiveIntegerField()
    SDS_P1 = serializers.DecimalField(max_digits=5, decimal_places=2)
    SDS_P2 = serializers.DecimalField(max_digits=5, decimal_places=2)
    BME280_temperature = serializers.DecimalField(max_digits=5, decimal_places=2)
    BME280_pressure = serializers.DecimalField(max_digits=8, decimal_places=2)
    BME280_humidity = serializers.DecimalField(max_digits=5, decimal_places=2)
    samples = serializers.IntegerField()
    min_micro = serializers.IntegerField()
    max_micro = serializers.IntegerField()
    interval = serializers.IntegerField()
    signal = serializers.IntegerField()

    class Meta:
        model = SensorData2
        fields = '__all__'