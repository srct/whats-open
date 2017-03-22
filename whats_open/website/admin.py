from django.contrib import admin
from website.models import Facility, Category, Schedule, OpenTime


class OpenTimeInline(admin.TabularInline):
    model = OpenTime
    fk_name = 'open_time_schedule'


class ScheduleAdmin(admin.ModelAdmin):
    inlines = [OpenTimeInline, ]


admin.site.register(Facility)
admin.site.register(Category)
admin.site.register(Schedule, ScheduleAdmin)
