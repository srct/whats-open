#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
api/serializers.py

Serializers allow complex data to be converted to native Python datatypes that
can then be easily rendered into JSON, XML or other content types.

http://www.django-rest-framework.org/api-guide/serializers
"""
# Other Imports
from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField

# App Imports
from .models import Category, Facility, Schedule, OpenTime, Location, Alert


class AlertSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = Alert
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        # Choose the model to be serialized
        model = Category
        # Serialize all of the fields
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Location model.
    """

    class Meta:
        # Choose the model to be serialized
        model = Location
        # Serialize all of the fields
        fields = "__all__"


class OpenTimeSerializer(serializers.ModelSerializer):
    """
    Serializer for the OpenTime model.
    """

    class Meta:
        # Choose the model to be serialized
        model = OpenTime
        # Serialize all of the fields
        fields = (
            "schedule",
            "modified",
            "start_day",
            "end_day",
            "start_time",
            "end_time",
        )


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
        fields = (
            "id",
            "open_times",
            "modified",
            "name",
            "valid_start",
            "valid_end",
            "twenty_four_hours",
            "schedule_for_removal",
            "promote_to_main",
        )


class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Facility model.

    From the docs:
        The HyperlinkedModelSerializer class is similar to the ModelSerializer
        class except that it uses hyperlinks to represent relationships, rather
        than primary keys.
        http://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer
    """

    # Append serialized objects
    facility_category = CategorySerializer(many=False, read_only=True)
    facility_location = LocationSerializer(many=False, read_only=True)
    main_schedule = ScheduleSerializer(many=False, read_only=True)
    special_schedules = ScheduleSerializer(many=True, read_only=True)
    facility_product_tags = TagListSerializerField()

    class Meta:
        # Choose the model to be serialized
        model = Facility
        # List the fields that we are serializing
        fields = (
            "slug",
            "facility_name",
            "logo",
            "facility_location",
            "facility_category",
            "phone_number",
            "facility_product_tags",
            "facility_classifier",
            "tapingo_url",
            "note",
            "main_schedule",
            "special_schedules",
            "modified",
        )
