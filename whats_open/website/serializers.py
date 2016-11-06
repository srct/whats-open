from rest_framework import serializers
from website.models import Category, Facility, Schedule, OpenTime

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

class OpenTimeSerializer(serializers.ModelSerializer):
    #schedule = serializers.RelatedField(many=False)
    schedule = serializers.RelatedField(read_only=True)
    class Meta:
        model = OpenTime

class ScheduleSerializer(serializers.ModelSerializer):
    #open_times = OpenTimeSerializer(many=True)
    open_times = OpenTimeSerializer(read_only=True)
    class Meta:
        model = Schedule

class FacilitySerializer(serializers.ModelSerializer):
    #category = serializers.RelatedField(many=False)
    category = serializers.RelatedField(read_only=True)
    #main_schedule = serializers.RelatedField(many=False)
    main_schedule = serializers.RelatedField(read_only=True)
    #special_schedules = serializers.RelatedField(many=True)
    special_schedules = serializers.RelatedField(read_only=True)

    class Meta:
        model = Facility

