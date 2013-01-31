$.ajax({
    url: '/ajax/schedule/',
}).done(function (data) {
    $('#grid').append('<div class="row"></div>');
    $.each(data.data, function (idx, restaurant) {
        if ($('#grid .row').last().children().length < 4) {
            $('#grid .row').append(
                '<div class="span3 closed" id="' + restaurant.id + '">' + restaurant.name + '</div>'
            );
        } else {
            $('#grid').append('<div class="row"></div>').append(
                '<div class="span3 closed" id="' + restaurant.id + '">' + restaurant.name + '</div>'
            );
        }
        var now = new Date();
        var schedule = undefined;
        $.each(restaurant.special_schedules, function (idx, special)  {
            if (now >= Date.parse(special.start)
                    && now <= Date.parse(special.end)) {
                schedule = special;
            }
        });
        if (schedule === undefined) {
            schedule = restaurant.main_schedule;
        }
        $.each(schedule.open_times, function (idx, time) {
            if (now >= Date.parse(time.start_time)
                    && now <= Date.parse(time.end_time)) {
                $('#grid #' + restaurant.id).removeClass('closed');
                $('#grid #' + restaurant.id).addClass('open');
            }
        });
    });
});
