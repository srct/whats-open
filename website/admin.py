from django.contrib import admin
from .models import Facility, Schedule, OpenTime

class OpenTimeAdmin(admin.ModelAdmin):
    pass
class FacilityAdmin(admin.ModelAdmin):
    pass
class ScheduleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Facility, FacilityAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(OpenTime, OpenTimeAdmin)
