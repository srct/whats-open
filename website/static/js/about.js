// Toggles the about page
$(document).ready(function(){
    var lastosition;
    $('#about-link').click(function(){
        // Keep track of the users vertical position so it can be scolled back
        //to when the window is closed
        position = $(window).scrollTop();
        console.log(position);
        $('#about-body').slideToggle(356);
        $('.main-container').toggleClass('grid-blur');
        $(this).parent().toggleClass('active');
        // Replace "About" link with the close icon
        $('#about-link-text, #about-close-nav').toggle();
        // Hide grid to disable scrolling when info body is active 
        // The delay prevents buggy scrolling on some mobile browsers                                      
        window.setTimeout(function() { $('.main-container').toggle() }, 350);
        $('html, body').animate({
            scrollTop: 0
        }, 500);
    });
    $('#about-close').click(function(){
        $('#about-link').parent().removeClass('active');
        $('#about-body').slideUp(356);
        $('.main-container').removeClass('grid-blur');
        $('body').removeClass('clip');
        $('#about-link-text').show();
        $('#about-close-nav').hide();
        $('.main-container').show();
        // Scroll back to saved position
        $('html, body').animate({
            scrollTop: position
        }, 500);
    });
});
