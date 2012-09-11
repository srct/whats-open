from django.db import models
from django.core.cache import cache


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    mainSchedule = models.ForeignKey('Schedule',
            related_name='restaurant_main')
    specialSchedules = models.ManyToManyField('Schedule',
            related_name='restaurant_special', null=True, blank=True)

    def save(self, *args, **kwargs):
        cache.clear()  # Invalidate cache on restaurant change/creation
        super(Restaurant, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        cache.clear()  # Invalidate cache on restuarant deletion
        super(Restaurant, self).delete(*args, **kwargs)


class Schedule(models.Model):
    name = models.CharField(max_length=100)
    dateValidStart = models.DateField(null=True, blank=True)
    dateValidEnd = models.DateField(null=True, blank=True)
    monOpen = models.TimeField(null=True, blank=True)
    monClose = models.TimeField(null=True, blank=True)
    tueOpen = models.TimeField(null=True, blank=True)
    tueClose = models.TimeField(null=True, blank=True)
    wedOpen = models.TimeField(null=True, blank=True)
    wedClose = models.TimeField(null=True, blank=True)
    thuOpen = models.TimeField(null=True, blank=True)
    thuClose = models.TimeField(null=True, blank=True)
    friOpen = models.TimeField(null=True, blank=True)
    friClose = models.TimeField(null=True, blank=True)
    satOpen = models.TimeField(null=True, blank=True)
    satClose = models.TimeField(null=True, blank=True)
    sunOpen = models.TimeField(null=True, blank=True)
    sunClose = models.TimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        cache.clear()  # Invalidate cache on schedule change/creation
        super(Schedule, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        cache.clear()  # Invalidate cache on schedule deletion
        super(Schedule, self).delete(*args, **kwargs)
