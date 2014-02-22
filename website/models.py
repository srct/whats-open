from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
import datetime

class Category(TimeStampedModel):
    name = models.CharField(max_length=100)

class Facility(TimeStampedModel):
    """Represents a facility location on campus."""
    name = models.CharField(max_length=100)
    owners = models.ManyToManyField(User)
    category = models.ForeignKey('Category')
    slug = AutoSlugField(populate_from='name',unique=True)
    on_campus = models.BooleanField(default=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    main_schedule = models.ForeignKey('Schedule',
            related_name='facility_main')
    special_schedules = models.ManyToManyField('Schedule',
            related_name='facility_special', null=True, blank=True)
     
    class Meta:
        verbose_name = "facility"
        verbose_name_plural = "facilities"
        # Sort by name in admin view
        ordering = ['name']

    def isOpen(self):
        """
        Return true if this facility is currently open.

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
                    else:
                        return False
        if self.main_schedule.isOpenNow():
            return True
        return False

    def __unicode__(self):
        return self.name

class Schedule(TimeStampedModel):
    """
    Contains opening and closing times for each day in a week.

    For special (temporary) schedules, start and end dates for
    when this schedule will be valid can also be set.

    """
    name = models.CharField(max_length=100)
    # inclusive:
    valid_start = models.DateField('Start Date', null=True, blank=True,
            help_text='Date that this schedule goes into effect')
    valid_end = models.DateField('End Date', null=True, blank=True,
            help_text='Last day that this schedule is in effect')
    
    class Meta:
        ordering = ['name']
        
    def isOpenNow(self):
        """Return true if this schedule is open right now."""
        for time in OpenTime.objects.filter(schedule=self):
            if time.isOpenNow():
                return True
        return False

    def __unicode__(self):
        return self.name


class OpenTime(TimeStampedModel):
    """Represents a period time when a Facility is open"""
    schedule = models.ForeignKey('Schedule', related_name='open_times')
    monday_start = models.TimeField()
    monday_end = models.TimeField()
    tuesday_start = models.TimeField()
    tuesday_end = models.TimeField()
    wednesday_start = models.TimeField()
    wednesday_end = models.TimeField()
    thursday_start = models.TimeField()
    thursday_end = models.TimeField()
    friday_start = models.TimeField()
    friday_end = models.TimeField()
    saturday_start = models.TimeField()
    saturday_end = models.TimeField()
    sunday_start = models.TimeField()
    sunday_end = models.TimeField()

    def isOpenNow(self):
        """Return true if the current time is this OpenTime's range"""
        today = datetime.datetime.today()
        if self.start_day <= self.end_day:
            if self.start_day == today.weekday():
                if self.start_time > today.time():
                    return False
            elif self.start_day > today.weekday():
                return False
            if self.end_day == today.weekday():
                if self.end_time < today.time():
                    return False
            elif self.end_day < today.weekday():
                return False
        else:
            if self.start_day == today.weekday():
                if self.start_time > today.time():
                    return False
            if self.end_day == today.weekday():
                if self.end_time < today.time():
                    return False
            if self.end_day < today.weekday() < self.start_day:
                return False
        return True

    def __unicode__(self):
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                'Saturday', 'Sunday']
        return '%s %s to %s %s' % (weekdays[self.start_day],
                self.start_time.strftime("%H:%M:%S"), weekdays[self.end_day],
                self.end_time.strftime("%H:%M:%S"))
