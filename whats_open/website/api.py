# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# Python stdlib Imports
import re

# App Imports
from .models import Facility

def export_data():
    facilities = list()
    
    # Sort the facilities by alphabetical order ignoring "the" and "a"
    alphalist = sorted(Facility.objects.all(),
            key=lambda r: re.sub('^(the|a) ', '', r.name, count=1,
            flags=re.IGNORECASE))
    
    for facility in alphalist:
        facility_data = {
            'name': facility.name,
            'location': facility.location, 
            'id': facility.id
        }
        open_times = list()
        # Sort open times by their start day and time
        sorted_times = sorted(facility.main_schedule.open_times.all(),
                key=lambda t: (t.start_day, t.start_time, t.end_time))
        for time in sorted_times:
            open_times.append({
                    'start_day': time.start_day,
                    'start_time': time.start_time.isoformat(),
                    'end_day': time.end_day,
                    'end_time': time.end_time.isoformat()
            })
        facility_data['main_schedule'] = {
                'name': facility.main_schedule.name,
                'open_times': open_times
        }
        special_schedules = list()
        for schedule in facility.special_schedules.all():
            open_times = list()
            sorted_times = sorted(schedule.open_times.all(),
                key=lambda t: (t.start_day, t.start_time, t.end_time))
            for time in sorted_times:
                open_times.append({
                        'start_day': time.start_day,
                        'start_time': time.start_time.isoformat(),
                        'end_day': time.end_day,
                        'end_time': time.end_time.isoformat()
                })
            special_schedules.append({
                    'name': schedule.name,
                    'start': schedule.valid_start.isoformat(),
                    'end': schedule.valid_end.isoformat(),
                    'open_times': open_times
            })
        facility_data['special_schedules'] = special_schedules
        facilities.append(facility_data)
    return facilities
