from django.db import models
from django.core.cache import cache
import datetime


class Restaurant(models.Model):
    """Represents a dining location on campus."""
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

    def isOpen(self):
        """
        Return true if this restaurant is currently open.

        First checks any valid special schedules and then checks the
        main default schedule.

        """
        today = datetime.datetime.today()
        for schedule in self.specialSchedules.all():
            if schedule.dateValidStart <= today <= schedule.dateValidEnd:
                if schedule.isOpenNow():
                    return True
        if self.mainSchedule.isOpenNow():
            return True
        return False


class Schedule(models.Model):
    """
    Contains opening and closing times for each day in a week.

    For special (temporary) schedules, start and end dates for
    when this schedule will be valid can also be set.

    """
    name = models.CharField(max_length=100)
    # inclusive:
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

    def isOpenNow(self):
        """Return true if this schedule is open right now."""
        today = datetime.datetime.today()
        weekday = today.weekday()
        if weekday == 0:
            start = self.monOpen
            end = self.monClose
        elif weekday == 1:
            start = self.tueOpen
            end = self.tueClose
        elif weekday == 2:
            start = self.wedOpen
            end = self.wedClose
        elif weekday == 3:
            start = self.thuOpen
            end = self.thuClose
        elif weekday == 4:
            start = self.friOpen
            end = self.friClose
        elif weekday == 5:
            start = self.satOpen
            end = self.satClose
        elif weekday == 6:
            start = self.sunOpen
            end = self.sunClose
        if (start is not None and end is not None and
                start <= today.time() <= end):
            return True
        else:
            return False
