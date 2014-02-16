from rest_framework import serializers
from website.models import Category, Facility, Schedule, OpenTime

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')
class FacilitySerializer(serializers.ModelSerializer):
    owner = serializers.RelatedField(many=True)
    main_schedule = serializers.RelatedField(many=False)
    special_schedule = serializers.RelatedField(many=False)
    class Meta:
        model = Facility
        fields = ('name', 'owner', 'slug', 'location', 'main_schedule', 'special_schedules')
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('name', 'valid_start', 'valid_end')
class OpenTimeSerializer(serializers.ModelSerializer):
    schedule = serializers.RelatedField(many=False)
    class Meta:
        model = OpenTime
        fields = ('start_day', 'start_time', 'end_day', 'end_time')
