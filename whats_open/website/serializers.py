from rest_framework import serializers
from website.models import Category, Facility, Schedule, OpenTime

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

class OpenTimeSerializer(serializers.ModelSerializer):
    schedule = serializers.RelatedField(many=False)
    class Meta:
        model = OpenTime

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule

class FacilitySerializer(serializers.ModelSerializer):
    category = serializers.RelatedField(many=False)
    main_schedule = serializers.RelatedField(many=False)
    special_schedules = serializers.RelatedField(many=True)

    class Meta:
        model = Facility

