from website.models import Restaurant


def export_data():
    restaurants = list()
    for restaurant in Restaurant.objects.all():
        restaurant_data = {'name': restaurant.name}
        open_times = list()
        for time in restaurant.main_schedule.open_times.all():
            open_times.append({
                    'start_day': time.start_day,
                    'start_time': time.start_time.isoformat(),
                    'end_day': time.end_day,
                    'end_time': time.end_time.isoformat()
            })
        restaurant_data['main_schedule'] = {
                'name': restaurant.main_schedule.name,
                'id': restaurant.id,
                'open_times': open_times
        }
        special_schedules = list()
        for schedule in restaurant.special_schedules.all():
            open_times = list()
            for time in schedule.open_times.all():
                open_times.append({
                        'start_day': time.start_day,
                        'start_time': time.start_time.isoformat(),
                        'end_day': time.end_day,
                        'end_time': time.end_time.isoformat()
                })
            special_schedules.append({
                    'name': schedule.name,
                    'id': restaurant.id,
                    'start': schedule.valid_start.isoformat(),
                    'end': schedule.valid_end.isoformat(),
                    'open_times': open_times
            })
        restaurant_data['special_schedules'] = special_schedules
        restaurants.append(restaurant_data)
    return restaurants
