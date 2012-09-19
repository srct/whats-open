from django.db import models
import datetime


class Restaurant(models.Model):
    """Represents a dining location on campus."""
    name = models.CharField(max_length=100)
    main_schedule = models.ForeignKey('Schedule',
            related_name='restaurant_main')
    special_schedules = models.ManyToManyField('Schedule',
            related_name='restaurant_special', null=True, blank=True)

    def isOpen(self):
        """
        Return true if this restaurant is currently open.

        First checks any valid special schedules and then checks the
        main default schedule.

        """
        today = datetime.datetime.today().date()
        # Check special schedules first
        for schedule in self.special_schedules.all():
            # Special schedules must have valid_start and valid_end set
            if schedule.valid_start and schedule.valid_end:
                if schedule.valid_start <= today <= schedule.valid_end:
                    if schedule.isOpenNow():
                        return True
        if self.main_schedule.isOpenNow():
            return True
        return False

    def __unicode__(self):
        return self.name


class Schedule(models.Model):
    """
    Contains opening and closing times for each day in a week.

    For special (temporary) schedules, start and end dates for
    when this schedule will be valid can also be set.

    """
    name = models.CharField(max_length=100)
    # inclusive:
    valid_start = models.DateField(null=True, blank=True)
    valid_end = models.DateField(null=True, blank=True)
    mon_open = models.TimeField(null=True, blank=True)
    mon_close = models.TimeField(null=True, blank=True)
    tue_open = models.TimeField(null=True, blank=True)
    tue_close = models.TimeField(null=True, blank=True)
    wed_open = models.TimeField(null=True, blank=True)
    wed_close = models.TimeField(null=True, blank=True)
    thu_open = models.TimeField(null=True, blank=True)
    thu_close = models.TimeField(null=True, blank=True)
    fri_open = models.TimeField(null=True, blank=True)
    fri_close = models.TimeField(null=True, blank=True)
    sat_open = models.TimeField(null=True, blank=True)
    sat_close = models.TimeField(null=True, blank=True)
    sun_open = models.TimeField(null=True, blank=True)
    sun_close = models.TimeField(null=True, blank=True)

    def isOpenNow(self):
        """Return true if this schedule is open right now."""
        today = datetime.datetime.today()
        weekday = today.weekday()
        days = [
                (self.mon_open, self.mon_close),
                (self.tue_open, self.tue_close),
                (self.wed_open, self.wed_close),
                (self.thu_open, self.thu_close),
                (self.fri_open, self.fri_close),
                (self.sat_open, self.sat_close),
                (self.sun_open, self.sun_close),
        ]
        start, end = days[weekday]
        if (start is not None and end is not None and
                start <= today.time() <= end):
            return True
        else:
            return False

    def __unicode__(self):
        return self.name
