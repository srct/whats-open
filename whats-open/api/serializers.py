"""
api/serializers.py

Serializers allow complex data to be converted to native Python datatypes that
can then be easily rendered into JSON, XML or other content types.

http://www.django-rest-framework.org/api-guide/serializers
"""
# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# App Imports
from .models import Category, Facility, Schedule, OpenTime, Location, Alert

# Other Imports
from rest_framework import serializers

class AlertSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Alert
        fields = '__all__'

class OpenTimeSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        # Choose the model to be serialized
        model = Category
        # Serialize all of the fields
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Location model.
    """
    class Meta:
        # Choose the model to be serialized
        model = Location
        # Serialize all of the fields
        fields = '__all__'

class OpenTimeSerializer(serializers.ModelSerializer):
    """
    Serializer for the OpenTime model.
    """
    class Meta:
        # Choose the model to be serialized
        model = OpenTime
        # Serialize all of the fields
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    """
    Serializer for the Schedule model.
    """
    # Append a serialized OpenTime object
    open_times = OpenTimeSerializer(many=True, read_only=True)

    class Meta:
        # Choose the model to be serialized
        model = Schedule
        # List the fields that we are serializing
        fields = ('id', 'open_times', 'modified', 'name', 'valid_start',
                  'valid_end')

class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Facility model.

    From the docs:
        The HyperlinkedModelSerializer class is similar to the ModelSerializer
        class except that it uses hyperlinks to represent relationships, rather
        than primary keys.
        http://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer
    """
    # Append a serialized Category object
    facility_category = CategorySerializer(many=False, read_only=True)
    # Append a serialized Location object
    facility_location = LocationSerializer(many=False, read_only=True)
    # Append a serialized Schedule object to represent main_schedule
    main_schedule = ScheduleSerializer(many=False, read_only=True)
    # Append a serialized Schedule object to represent special_schedules
    special_schedules = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        # Choose the model to be serialized
        model = Facility
        # List the fields that we are serializing
        fields = ('id', 'facility_category', 'facility_location',
                  'main_schedule', 'special_schedules', 'modified', 'name')
