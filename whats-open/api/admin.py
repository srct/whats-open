#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
api/admin.py

Django admin interface configuration.

https://docs.djangoproject.com/en/1.11/ref/contrib/admin/
"""
# Django Imports
from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
# App Imports
from .models import Facility, Schedule, OpenTime, Category, Location, Alert

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    """
    Custom Admin panel for the Facility model.

    Allows admins to create new facilities through the admin interface.
    """
    def drop_special_schedules(modeladmin, request, queryset):
        for facility in queryset:
            facility.special_schedules.clear()

    actions = [drop_special_schedules, ]

    # Allow filtering by the following fields
    list_filter = ['facility_category', 'facility_location']
    # Modify the rendered layout of the "create a new facility" page
    # We are basically reordering things to look nicer to the user here
    fieldsets = (
        (None, {
            'fields': ('facility_name', 'logo', 'facility_category',
                       'facility_location', 'main_schedule', 'special_schedules',
                       ('facility_product_tags', 'facility_labels',
                        'facility_classifier'),
                       'tapingo_url', 'phone_number', 'note', 'owners'),
        }),
    )

class OpenTimeInline(admin.TabularInline):
    """
    A table of time periods that represent an "open time" for a Facility.

    https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#django.contrib.admin.TabularInline
    """
    # Columns correspond to each attribute in the OpenTime table
    model = OpenTime
    # 7 days of the week, so only have 7 rows
    max_num = 7
    extra = 7
    # We are basically reordering things to look nicer to the user here
    fieldsets = (
        (None, {
            'fields': (
                ('start_day', 'start_time'),
                ('end_day', 'end_time')
            ),
        }),
    )

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """
    Custom Admin panel for the Schedule model.

    Allows admins to create new schedules through the admin interface.
    Additionally, we append the OpenTimeInline table to allow for open times to
    be defined for the schedule we are creating.
    """
    # Allow filtering by the following fields
    list_display = ['name', 'modified']
    # Append the OpenTimeInline table to the end of our admin panel
    inlines = [OpenTimeInline, ]
    # Modify the rendered layout of the "create a new facility" page
    fieldsets = (
        (None, {
            'fields': ('name',
                       # Pair valid_start and valid_end together on the same
                       # line
                       ('valid_start', 'valid_end'),
                       'twenty_four_hours',
                       'schedule_for_removal',
                       'promote_to_main')
        }),
    )

# https://docs.djangoproject.com/en/1.11/ref/contrib/gis/admin/#osmgeoadmin
OSMGeoAdmin.default_lon = -8605757.16502
OSMGeoAdmin.default_lat = 4697457.00333
OSMGeoAdmin.default_zoom = 15
admin.site.register(Location, OSMGeoAdmin)
# Use the default ModelAdmin interface for these
admin.site.register(Category)
admin.site.register(Alert)
