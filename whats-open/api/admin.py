"""
api/admin.py

Django admin interface configuration.

https://docs.djangoproject.com/en/1.11/ref/contrib/admin/
"""
# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# Django Imports
from django.contrib import admin

# App Imports
from .models import Facility, Schedule, OpenTime, Category, Location

class FacilityAdmin(admin.ModelAdmin):
    """
    """
    model = Facility
    list_display = ['name', ]
    list_filter = ['facility_category', 'facility_location']
    fieldsets = (
        (None, {
            'fields': ('name', 'facility_category', 'facility_location',
                       'main_schedule', 'special_schedules', 'owners'),
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

class ScheduleAdmin(admin.ModelAdmin):
    """
    """
    list_display = ['name', 'modified']
    inlines = [OpenTimeInline, ]
    fieldsets = (
        (None, {
            'fields': ('name',
                       # Pair valid_start and valid_end together on the same
                       # line
                       ('valid_start', 'valid_end'))
        }),
    )

# Register the administration panels
# https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#modeladmin-objects
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Schedule, ScheduleAdmin)
# Use the default ModelAdmin interface for these
admin.site.register(Category)
admin.site.register(Location)
