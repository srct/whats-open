from rest_framework import serializers
from website.models import Category, Facility, Schedule, OpenTime

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class OpenTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenTime
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    open_times = OpenTimeSerializer(many=True, read_only=True)
    class Meta:
        model = Schedule
        fields = '__all__'

class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    main_schedule = ScheduleSerializer(many=False, read_only=True)
    special_schedules = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Facility
        fields = '__all__'

