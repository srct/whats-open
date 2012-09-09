from django.db import models
import datetime

class Restaurant(models.Model):
    name = models.CharField(max_length = 100)
    mainSchedule = models.ForeignKey('Schedule', related_name = 'restaurant_main')
    specialSchedules = models.ManyToManyField('Schedule', related_name = 'restaurant_special', null = True, blank = True)

    #function
    #def analyzer(dayOpen, dayClose):
    #   if dayOpen is null or dayClose is null:
    #       return False
    #   elif timeNow >= dayOpen and timeNow <= dayClose:
    #       return True
    #   else:
    #       return False

    def isOpen():
        timeNow = datetime.datetime.now().time()
        day = datetime.date.today().weekday()
        if day is 1:
            if monOpen is null or monClose is null:
                return False
            elif timeNow >= monOpen and timeNow <= monClose:
                return True
            else:
                return False
        elif day is 2:
            if tueOpen is null or tueClose is null:
                return False
            elif timeNow >= tueOpen and timeNow <= tueClose:
                return True
            else:
                return False
        elif day is 3:
            if wedOpen is null or wedClose is null:
                return False
            elif timeNow >= wedOpen and timeNow <= wedClose:
                return True
            else:
                return False
        elif day is 4:
            if thuOpen is null or thuClose is null:
                return False
            elif timeNow >= thuOpen and timeNow <= thuClose:
                return True
            else:
                return False
        elif day is 5:
            if friOpen is null or friClose is null:
                return False
            elif timeNow >= friOpen and timeNow <= friClose:
                return True
            else:
                return False
        elif day is 6:
            if satOpen is null or satClose is null:
                return False
            elif timeNow >= satOpen and timeNow <= satClose:
                return True
            else:
                return False
        elif day is 7:
            if sunOpen is null or sunClose is null:
                return False
            elif timeNow >= sunOpen and timeNow <= sunClose:
                return True
            else:
                return False

    #def isC`losing:



class Schedule(models.Model):
    name = models.CharField(max_length = 100)
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
    
