# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# Django Imports
from django.contrib import admin

# App Imports
from .models import Facility, Schedule, OpenTime, Category

class OpenTimeInline(admin.TabularInline):
    model = OpenTime
    fk_name = 'schedule'
    max_num = 7

class OpenTimeAdmin(admin.ModelAdmin):
    pass

class FacilityAdmin(admin.ModelAdmin):
    model = Facility
    list_display = ['name', 'location' ]
    list_filter = ['facility_category', ]
    fieldsets = (
        (None, {
             'fields': ('name', 'facility_category',
                        ('location', 'on_campus'),
                        'main_schedule', 'special_schedules', ),
        }),
        ('Advanced', {
             'fields': ('owners', ),
             'classes': ('collapse', ),
        }),
    )

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['name', 'modified']
    inlines = [OpenTimeInline, ]
    fieldsets = (
        (None, {
             'fields': ('name',
                       ('valid_start', 'valid_end'),)
               }),
    )

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Facility, FacilityAdmin)
admin.site.register(Schedule, ScheduleAdmin)
#admin.site.register(OpenTime, OpenTimeAdmin)
admin.site.register(Category, CategoryAdmin)
