"""
api/models.py

Define the objects that will be stored in the database and later served through
the API.

https://docs.djangoproject.com/en/1.11/topics/db/models/
"""
# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# Python stdlib Imports
import datetime

# Django Imports
from django.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Other Imports
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from taggit.managers import TaggableManager

class Category(TimeStampedModel):
    """
    Represents the "category" that a Facility falls under. A Category is a
    grouping of Facilities that serve a common/similar purpose.

    ex.
    - Dining
    - Gyms
    - Study areas (Libraries, The Ridge, JC, etc)
    """
    # The name of the category
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        # Sort by name in admin view.
        ordering = ['name']

    def __str__(self):
        """
        String representation of a Category object.
        """
        return self.name

class Location(TimeStampedModel):
    """
    Represents a specific location that a Facility can be found.
    """
    # The building that the facility is located in (on campus).
    building = models.CharField(max_length=100)
    # The physical address of the facility.
    address = models.CharField(max_length=100)
    # Boolean for whether or not the location is "on campus" or not.
    on_campus = models.BooleanField(default=True)
    # A GeoJson coordinate pair that represents the physical location
    coordinate_location = PointField()

    class Meta:
        verbose_name = "location"
        verbose_name_plural = "locations"

    def __str__(self):
        """
        String representation of a Location object.
        """
        return 'Found in %s at %s | On Campus: %s' % (self.building,
                                                      self.address,
                                                      self.on_campus)

class Facility(TimeStampedModel):
    """
    Represents a specific facility location. A Facility is some type of
    establishment that has a schedule of open hours and a location that serves
    a specific purpose that can be categorized.
    """
    # The name of the Facility
    name = models.CharField(max_length=100)
    # Instead of id
    slug = AutoSlugField(populate_from='name', unique=True)

    # The category that this facility can be grouped with
    facility_category = models.ForeignKey('Category',
                                          related_name="categories")
    # The location object that relates to this facility
    facility_location = models.ForeignKey('Location',
                                          related_name="facilities")

    # The User(s) that claim ownership over this facility
    owners = models.ManyToManyField(User)

    # The schedule that is defaulted to if no special schedule is in effect
    main_schedule = models.ForeignKey('Schedule',
                                      related_name='facility_main')
    # A schedule that has a specific start and end date
    special_schedules = models.ManyToManyField('Schedule',
                                               related_name='facility_special',
                                               blank=True,
                                               help_text="""This schedule will
                                                            come into effect
                                                            only for its
                                                            specified duration.
                                                            """)
    # URL, if it exists, to the Tapingo page that is associated with this
    # facility
    tapingo_url = models.URLField(blank=True, validators=[RegexValidator(regex='^https:\/\/www.tapingo.com\/',
                                                                         message='The link is not a valid tapingo link. Example: https://www.tapingo.com/order/restaurant/starbucks-gmu-johnson/',
                                                                         code='invalid_tapingo_url')])
    # A comma seperate list of words that neatly an aptly describe the product
    # that this facility produces. (ex. for Taco Bell: mexican, taco, cheap)
    facility_product_tags = TaggableManager()

    def is_open(self):
        """
        Return true if this facility is currently open.

        First checks any valid special schedules and then checks the main,
        default, schedule.
        """
        # Get the current date
        today = datetime.datetime.today().date()
        # Check special schedules first, loop through all of them
        for schedule in self.special_schedules.all():
            # Special schedules must have valid_start and valid_end set
            if schedule.valid_start and schedule.valid_end:
                # If a special schedule in in effect
                if schedule.valid_start <= today <= schedule.valid_end:
                    # Check if the facility is open or not based on that 
                    # special schedule
                    if schedule.is_open_now():
                        # Open
                        return True
                    else:
                        # Closed
                        return False
        # If no special schedule is in effect then check if the facility is
        # open using the main_schedule
        if self.main_schedule.is_open_now():
            # Open
            return True
        else:
            # Closed
            return False

    def clean_special_schedules(self):
        """
        Loop through every special_schedule and remove entries that have
        expired.
        """
        for special_schedule in self.special_schedules.all():
            # If it ends before today
            if special_schedule.valid_end < datetime.date.today():
                self.special_schedules.remove(special_schedule)

    class Meta:
        verbose_name = "facility"
        verbose_name_plural = "facilities"
        # Sort by name in admin view
        ordering = ['name']

    def __str__(self):
        """
        String representation of a Facility object.
        """
        return self.name

class Schedule(TimeStampedModel):
    """
    A period of time between two dates that represents the beginning and end of
    a "schedule" or rather, a collection of open times for a facility.
    """
    # The name of the schedule
    name = models.CharField(max_length=100)

    # The start date of the schedule
    # (inclusive)
    valid_start = models.DateField('Start Date', null=True, blank=True,
                                   help_text="""Date that this schedule goes
                                                into effect""")
    # The end date of the schedule
    # (inclusive)
    valid_end = models.DateField('End Date', null=True, blank=True,
                                 help_text="""Last day that this schedule is
                                              in effect""")

    def is_open_now(self):
        """
        Return true if this schedule is open right now.
        """
        # Loop through all the open times that correspond to this schedule
        for open_time in OpenTime.objects.filter(schedule=self):
            # If the current time we are looking at is open, then the schedule 
            # will say that the facility is open
            if open_time.is_open_now():
                # Open
                return True
        # Closed (all open times are not open)
        return False

    class Meta:
        # Sort by name in admin view
        ordering = ['name']

    def __str__(self):
        """
        String representation of a Schedule object.
        """
        return self.name


class OpenTime(TimeStampedModel):
    """
    Represents a time period when a Facility is open.

    Monday = 0, Sunday = 6.
    """
    # Define integer constants to represent days of the week
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

    # Tuple that ties a day of the week with an integer representation
    DAY_CHOICES = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    )

    # The schedule that this period of open time is a part of
    schedule = models.ForeignKey('Schedule', related_name='open_times')

    # The day that the open time begins on
    start_day = models.IntegerField(default=0, choices=DAY_CHOICES)
    # The day that the open time ends on
    end_day = models.IntegerField(default=0, choices=DAY_CHOICES)

    # The time of day that the open time begins at
    start_time = models.TimeField()
    # The time of day that the open time ends
    end_time = models.TimeField()

    def is_open_now(self):
        """
        Return true if the current time is this OpenTime's range.
        """
        # Get the current datetime
        today = datetime.datetime.today()
        # Check that the start occurs before the end
        if self.start_day <= self.end_day:
            # If today is the start_day
            if self.start_day == today.weekday():
                # If the start_time has not occurred
                if self.start_time > today.time():
                    # Closed
                    return False
            # If the start_day has not occurred
            elif self.start_day > today.weekday():
                # Closed
                return False
            # If the end_day is today
            if self.end_day == today.weekday():
                # If the end_time has already occurred
                if self.end_time < today.time():
                    # Closed
                    return False
            # If the end_day has already occurred
            elif self.end_day < today.weekday():
                # Closed
                return False
        # The end_day > start_day
        else:
            # If today is the start_day
            if self.start_day == today.weekday():
                # If the start_time has not occurred
                if self.start_time > today.time():
                    # Closed
                    return False
            # If the end_day is today
            if self.end_day == today.weekday():
                # If the end_time has already occurred
                if self.end_time < today.time():
                    # Closed
                    return False
            # If the current date takes place after the end_date but before
            # start_day
            if self.end_day < today.weekday() < self.start_day:
                # Closed
                return False
        # All checks passed, it's Open
        return True

    def __str__(self):
        """
        String representation of a OpenTime object.
        """
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday']
        return '%s %s to %s %s' % (weekdays[self.start_day],
                                   self.start_time.strftime("%H:%M:%S"),
                                   # to
                                   weekdays[self.end_day],
                                   self.end_time.strftime("%H:%M:%S"))

class Alert(TimeStampedModel):
    """
    Some type of notification that is displayed to clients that conveys a
    message. Past examples include: random closings, modified schedules being
    in effect, election reminder, advertising for other SRCT projects.

    Alerts last for a period of time until the information is no longer dank.
    """
    # Define string constants to represent urgency tag levels
    INFO = 'info'  # SRCT announcements
    MINOR = 'minor'  # Holiday hours are in effect
    MAJOR = 'major'  # The hungry patriot is closed today
    EMERGENCY = 'emergency'  # Extreme weather

    # Tuple that ties a urgency tag with a string representation
    URGENCY_CHOICES = (
        (INFO, 'Info'),
        (MINOR, 'Minor'),
        (MAJOR, 'Major'),
        (EMERGENCY, 'Emergency'),
    )

    # The urgency tag for this Alert
    urgency_tag = models.CharField(max_length=10, default='Info',
                                   choices=URGENCY_CHOICES)

    # The text that is displayed that describes the Alert
    message = models.CharField(max_length=140)

    # The date + time that the alert will be start being served
    start_datetime = models.DateTimeField()

    # The date + time that the alert will stop being served
    end_datetime = models.DateTimeField()

    def __str__(self):
        """
        String representation of an Alert object.
        """
        return "%s" % (self.message)
