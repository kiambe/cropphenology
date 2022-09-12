from rest_framework import serializers
from planting.models import *
class PlantingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantingDatePlannerC
        fields = "__all__"
        depth = 1