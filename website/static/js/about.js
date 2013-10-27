$(document).ready(function(){
    $('#about-link').click(function(){
         $(this).parent().toggleClass('active');
         $('#about-body').slideToggle(356);
         $('.main-container').toggleClass('grid-blur');
         // Prevent body from scolling when about section is active
         $('body').toggleClass('clip');
         $('#about-link-text, #about-close-nav').toggle();
    });
    $('#about-close').click(function(){
         $('#about-link').parent().removeClass('active');
         $('#about-body').slideUp(356);
         $('.main-container').removeClass('grid-blur');
         $('body').removeClass('clip');
         $('#about-link-text').show();
         $('#about-close-nav').hide();
    });
});
