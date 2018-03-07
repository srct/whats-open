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
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render
# App Imports
from .models import Facility, Schedule, OpenTime, Category, Location, Alert


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    """
    Custom Admin panel for the Facility model.

    Allows admins to create new facilities through the admin interface.
    """
    def drop_special_schedules(self, request, queryset):
        num = queryset.count()
        for facility in queryset:
            facility.special_schedules.clear()
        self.message_user(request,
                          "Successfully cleared all special schedules for %d facilities." % num)
    drop_special_schedules.short_description = 'Clear all special schedules'

    def assign_bulk_schedules(self, request, queryset):
        num = queryset.count()
        # all admin actions-related requests are post requests, so we're looking for
        # the one that has the associated value with our confirmation input button
        if 'bulk_schedule' in request.POST:
            try:
                new_schedule = Schedule.objects.get(pk=request.POST['schedule'])
                name = new_schedule.name
                for facility in queryset:
                   facility.main_schedule = new_schedule
                   facility.save()
                self.message_user(request,
                                  "Set %s as the main schedule for %d facilities." % (name, num))
            except ObjectDoesNotExist:
                self.message_user(request,
                                  "Unable to set a new main schedule for %d facilities." % num)
            return HttpResponseRedirect(request.get_full_path())
        return render(request,
                      'bulk_schedules_intermediate.html',
                      context = {'facilities': queryset,
                                 'schedules': Schedule.objects.all()})
    assign_bulk_schedules.short_description = 'Set a main schedule for multiple facilities'

    def assign_bulk_special_schedules(self, request, queryset):
        num = queryset.count()
        if 'bulk_special_schedule' in request.POST:
            try:
                new_special_schedule = Schedule.objects.get(pk=request.POST['special_schedule'])
                name = new_special_schedule.name
                for facility in queryset:
                   facility.special_schedules.add(new_special_schedule)
                   facility.save()
                self.message_user(request,
                                  "Added %s as a special schedule to %d facilities." % (name, num))
            except ObjectDoesNotExist:
                self.message_user(request,
                                  "Unable to add additional special schedule to %d facilities." % num)
            return HttpResponseRedirect(request.get_full_path())
        return render(request,
                      'bulk_special_schedules_intermediate.html',
                      context = {'facilities': queryset,
                                 'schedules': Schedule.objects.all()})
    assign_bulk_special_schedules.short_description = 'Add a special schedule to multiple facilities'

    # a list of all actions to be added
    actions = [drop_special_schedules,
               assign_bulk_schedules, assign_bulk_special_schedules ]

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
