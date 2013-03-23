$.ajax({
    url: '/ajax/schedule/',
}).done(function (data) {
	//collecting list of restaurant names from server data	
	var restaurants = [];
	
	for (var i = 0; i < data.data.length; i++) {
		restaurants.push(data.data[i].name);
	};
	//Monitors for keyboard activity to detect when the input field is empty
    $('#searchBar').keyup(function() {
		var value = $('#searchBar').val();
		if (value == 0){
			//resets all backgrounds to white if the search bar is empty 
			$('.opened').css('background-color','white');
			$('.closed').css('background-color','white');
		}	  
	});	   	
	// For doumentation on jQuery's autocomplete: (api.jqueryui.com/autocomplete)     	 	
    $("#searchBar").autocomplete({  
    	source: restaurants,
    	//making it so the search result list doesn't physically appear 
    	messages: { 
        	noResults: '',
        	results: function(){} 
        },
        response: function(event, ui) {
			//resets all backgrounds to white if the search bar is edited 
			$('.opened').css('background-color','white');
			$('.closed').css('background-color','white');
			//ui.content array contains all names that are returned from the search
			for (var result in ui.content){
				//Highlights all search results	
				$('.opened:contains("'+ui.content[result].value+'")').css('background-color','#FDFFBF');
				$('.closed:contains("'+ui.content[result].value+'")').css('background-color','#FDFFBF');
			}
            // To prevent the page width from extending
            $('.ui-autocomplete').remove();
		}
	});
});
