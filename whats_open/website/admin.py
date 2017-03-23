from django.contrib import admin
from .models import Facility, Schedule, OpenTime, Category

class OpenTimeInline(admin.TabularInline):
    model = OpenTime
    fk_name = 'schedule'

class OpenTimeAdmin(admin.ModelAdmin):
    pass

class FacilityAdmin(admin.ModelAdmin):
    pass

class ScheduleAdmin(admin.ModelAdmin):
    inlines = [OpenTimeInline, ]

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Facility, FacilityAdmin)
admin.site.register(Schedule, ScheduleAdmin)
#admin.site.register(OpenTime, OpenTimeAdmin)
admin.site.register(Category, CategoryAdmin)
