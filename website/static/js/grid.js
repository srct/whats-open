var restaurants = [];

function sort_restaurants(filtered_restaurants) {
    var open = $.grep(filtered_restaurants, 
            function (r, idx) { return (r.open === true) });
    var closed = $.grep(filtered_restaurants, 
            function (r, idx) { return (r.open === false) });
    return $.merge(open, closed);
}

function construct_grid(filtered_restaurants) {
    // Hide footer while generating grid to prevent it flying across the screen
    $('#footer').hide();
    $('#grid').empty();
    $('#grid').html('<div class="row"></div>');
    if (filtered_restaurants.length == 0) {
        $('#grid').append('<span class="col-md-2 offset5">No results found.</span>');
        return;
    }
    sorted_restaurants = sort_restaurants(filtered_restaurants);
    $.each(sorted_restaurants, function (idx, restaurant) {
        var open_class = 'closed';
        if (restaurant.open) {
            open_class = 'opened';
        }
        // Append the data into the Bootstrap scaffolding
        $('#grid .row').last().append(
            '<div class="col-sm-6 col-md-4 col-lg-3 grid-box id="' + restaurant.id + '">\
                <div class="restaurant ' + open_class + '">' + restaurant.name + '</div>\
            </div>'
        );
    });
    $('#footer').show();
}

$.ajax({
    url: '/ajax/schedule/',
}).done(function (data) {
    restaurants = data.data;
    $.each(restaurants, function (idx, restaurant) {
        var now = new Date();
        var date = new Date().setHours(0,0,0,0);
        // JavaScript sets 0 to Sunday instead of Monday
        var day = now.getDay() - 1;
        if (day === -1) {
            day = 6;
        }
        var schedule = undefined;
        // If there exists a valid special schedule choose it.
        $.each(restaurant.special_schedules, function (idx, special)  {
            if (day >= Date.parse(special.start)
                    && day <= Date.parse(special.end)) {
                schedule = special;
            }
        });
        // If there was no special schedule, then use main_schedule.
        if (schedule === undefined) {
            schedule = restaurant.main_schedule;
        }
        // Open the restaurants that are open, leave the rest closed.
        $.each(schedule.open_times, function (idx, time) {
            var start_day = time.start_day;
            var end_day = time.end_day;
            var start_time = Date.parse(time.start_time);
            var end_time = Date.parse(time.end_time);
            if (day === start_day) {
                if (now >= Date.parse(time.start_time)) {
                    if (day === end_day) {
                        if (now <= Date.parse(time.end_time)) {
                            restaurant.open = true;
                            return false;
                        }
                    } else {
                        restaurant.open = true;
                        return false;
                    }

                }
            } else if (day === end_day) {
                if (now <= Date.parse(time.end_time)) {
                    if (day === start_day) {
                        if (now >= Date.parse(time.start_time)) {
                            restaurant.open = true;
                            return false;
                        }
                    } else {
                        restaurant.open = true;
                        return false;
                    }
                }
            } else if (start_day < end_day) {
                if (day > start_day && day < end_day) {
                    restaurant.open = true;
                    return false;
                }
            } else if (start_day > end_day) {
                if (day < start_day || day > end_day) {
                    restaurant.open = true;
                    return false;
                }
            }
            restaurant.open = false;
        });
    });
    construct_grid(restaurants);
});
