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
    open_times = OpenTimeSerializer(many=True)
    class Meta:
        model = Schedule

class FacilitySerializer(serializers.ModelSerializer):
    main_schedule = ScheduleSerializer()
    special_schedules = ScheduleSerializer(many=True)

    class Meta:
        model = Facility

