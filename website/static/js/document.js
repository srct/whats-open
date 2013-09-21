$(document).ready(function() {
    var lastClicked = null;
    $('#info-body').click(function() {
       $(this).slideUp(350); 
    });
    $(document).on('click', '.grid-box', function(){
        $('#info-body').slideDown(350);
    });
});