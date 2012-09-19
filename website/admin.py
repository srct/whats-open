from django.contrib import admin
from website.models import Restaurant, Schedule, OpenTime


class OpenTimeInline(admin.TabularInline):
    model = OpenTime


class ScheduleAdmin(admin.ModelAdmin):
    inlines = [OpenTimeInline, ]


admin.site.register(Restaurant)
admin.site.register(Schedule, ScheduleAdmin)
