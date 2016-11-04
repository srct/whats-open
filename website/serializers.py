from rest_framework import serializers
from website.models import Category, Facility, Schedule, OpenTime

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule

class OpenTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenTime
