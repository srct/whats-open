from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length = 100)
    mainSchedule = models.ForeignKey('Schedule', related_name = 'restaurant_main')
    specialSchedules = models.ManyToManyField('Schedule', related_name = 'restaurant_special')

class Schedule(models.Model):
    dateValidStart = models.DateField(null = True, blank = True)
    dateValidEnd = models.DateField(null = True, blank = True)
    monOpen = models.TimeField(null = True, blank = True)
    monClose = models.TimeField(null = True, blank = True)
    tueOpen = models.TimeField(null = True, blank = True)
    tueClose = models.TimeField(null = True, blank = True)
    wedOpen = models.TimeField(null = True, blank = True)
    wedClose = models.TimeField(null = True, blank = True)
    thuOpen = models.TimeField(null = True, blank = True)
    thuClose = models.TimeField(null = True, blank = True)
    friOpen = models.TimeField(null = True, blank = True)
    friClose = models.TimeField(null = True, blank = True)
    satOpen = models.TimeField(null = True, blank = True)
    satClose = models.TimeField(null = True, blank = True)
    sunOpen = models.TimeField(null = True, blank = True)
    sunClose = models.TimeField(null = True, blank = True)
    
