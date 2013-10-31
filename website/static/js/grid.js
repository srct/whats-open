var restaurants = [];

function correct_grid_overflow(){
    // This function ensures that all text inside the grid-boxes display nicely on one line. 
    $('.restaurant').css('font-size', '');
    $('.restaurant').each(function() {
        // Overflow is detected if the height of the box is less than
        // the clipped scroll height of the box.
        while ($(this).height() > 0 && $(this).outerHeight() < $(this)[0].scrollHeight) {
            // Shrink the elements that overflow until their contents fit on one line.
            var newSize = parseInt($(this).css('font-size')) - 1;
            $(this).css('font-size', newSize + 'px');
            $(this).children('.building').css('font-size', newSize - 6 + 'px');
            // Calulated padding is added to ensure the text remains vertically centered.
            $(this).css('padding-top', 31 - newSize + 'px');
        }    
    });
}

function sort_restaurants(filtered_restaurants) {
    var open = $.grep(filtered_restaurants, 
            function (r, idx) { return (r.open === true) });
    var closed = $.grep(filtered_restaurants, 
            function (r, idx) { return (r.open === false) });
    return $.merge(open, closed);
}

function construct_grid(filtered_restaurants) {
    $('#grid').empty();
    $('#grid').html('<div class="row"></div>');
    if (filtered_restaurants.length == 0) {
        $('#grid').append('<span class="col-md-8 offset2 grid-box" id="no-results">No results found.</span>');
        $('#grid').show();
        return;
    }
    sorted_restaurants = sort_restaurants(filtered_restaurants);
    $.each(sorted_restaurants, function (idx, restaurant) {
        var open_class = 'closed';
        if (restaurant.open) {
            open_class = 'opened';
        }
        // Append the data into the grid scaffolding.
        // Note that identical restaurants can be labeled via location. If there text in square brackets 
        // next to a restuarant name, the text will be formatted as next to it. 
        $('#grid .row').append(
            '<div class="col-sm-6 col-md-4 col-lg-3 grid-box" id="' + restaurant.id + '">\
                <div class="restaurant ' + open_class + '">' + 
                    restaurant.name.replace(/ ?\[(.+)\]/, '<span class="building"> ($1)</span>') + 
                '</div>\
            </div>'
        );
    });
    $('#grid').show();
    correct_overflow();
}

function update_grid(restaurants) {
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
                            restaurant.current = time;
                            return false;
                        }
                    } else {
                        restaurant.open = true;
                        restaurant.current = time;
                        return false;
                    }

                }
            } else if (day === end_day) {
                if (now <= Date.parse(time.end_time)) {
                    if (day === start_day) {
                        if (now >= Date.parse(time.start_time)) {
                            restaurant.open = true;
                            restaurant.current = time;
                            return false;
                        }
                    } else {
                        restaurant.open = true;
                        restaurant.current = time;
                        return false;
                    }
                }
            } else if (start_day < end_day) {
                if (day > start_day && day < end_day) {
                    restaurant.open = true;
                    restaurant.current = time;
                    return false;
                }
            } else if (start_day > end_day) {
                if (day < start_day || day > end_day) {
                    restaurant.open = true;
                    restaurant.current = time;
                    return false;
                }
            }
            restaurant.open = false;
        });
    });
}

$.ajax({
    url: '/ajax/schedule/',
}).done(function (data) {
    restaurants = data.data;
    update_grid(restaurants);
    construct_grid(restaurants);
    // Every second, check and see if it is necessary to update the grid. 
    var last_updated = new Date();
    setInterval(function(){
    	now = new Date();
    	// If the hour has changed, it the half hour has changed 
    	// or it has been over a half hour (180000 milliseconds) since the last update.
    	if (last_updated.getHours() != now.getHours() ||
    	   (last_updated.getMinutes() < 30 && now.getMinutes() >= 30) || now - last_updated > 1800000){
	    	update_grid(restaurants);
	    	construct_grid(restaurants);
	    	last_updated = new Date(); 
    	}
    }, 1000);
    $(window).on('resize', function(){
        correct_grid_overflow();
    });
});
