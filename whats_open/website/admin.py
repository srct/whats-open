from django.contrib import admin
from .models import Facility, Schedule, OpenTime, Category


class OpenTimeInline(admin.TabularInline):
    model = OpenTime
    fk_name = 'schedule'
    max_num = 7


class OpenTimeAdmin(admin.ModelAdmin):
    pass


class CampusFilter(admin.SimpleListFilter):
    title = 'campus'
    parameter_name = 'campus'

    def lookups(self, request, model_admin):
        return Facility.CAMPUS_CHOICES

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(campus=self.value())
        else:
            return queryset


class FacilityAdmin(admin.ModelAdmin):
    model = Facility
    list_display = ['name', 'location' ]
    list_filter = ['facility_category', CampusFilter]
    fieldsets = (
        (None, {
             'fields': ('name', 'facility_category',
                        ('campus', 'location'),
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
