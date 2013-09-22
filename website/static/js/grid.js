var restaurants = [];

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
        $('#grid').append('<span class="col-md-2 offset5" id="no-results">No results found.</span>');
        $('#footer').show();
        return;
    }
    sorted_restaurants = sort_restaurants(filtered_restaurants);
    $.each(sorted_restaurants, function (idx, restaurant) {
        var open_class = 'closed';
        if (restaurant.open) {
            open_class = 'opened';
        }
        // Append the data into the Bootstrap scaffolding
        $('#grid .row').append(
            '<div class="col-sm-6 col-md-4 col-lg-3 grid-box" id="' + restaurant.id + '">\
                <div class="restaurant ' + open_class + '">' + restaurant.name + '</div>\
            </div>'
        );
    });
    $('#footer').show();
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
});
$(document).ready(function() {
    var lastClicked = null;
    $('#info-body').click(function() {
       $(this).slideUp(350); 
    });
    $(document).on('click', '.grid-box', function() {
        // If the user clicks on the same box twice it will close the info menu
        grid_id = $(this).attr('id');
        if (lastClicked == grid_id){
            $('#info-body').slideToggle(300)
        }
        else {
            $('#info-body').slideDown(300);
            lastClicked = grid_id;
        }
        // Search though the restaurnts object to find the selected restaurant's info
        var restaurant;
        $.each(restaurants, function(idx, restaurant_i) { 
            if (restaurant_i.id == grid_id) {
                restaurant = restaurant_i;
                return false;
            }
        });
        // Display restaurant info in the info-body
        $('#info-name').text(restaurant.name);
        if (restaurant.open){
            $('#info-status').html('<b>Status:</b>  Open');
            var closing = Date.parse(restaurant.current.end_time);
            $('#info-next').html('<b>Open Till:</b> ' + closing.toLocaleTimeString().replace(/:\d+ /, ' '));
        }
        else {
            $('#info-status').html('<b>Status:</b>  Closed');
            $('#info-next').html("");
        }
    });
});
