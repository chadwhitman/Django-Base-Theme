// Place any custom jQuery here //

(function () {
	$('#top-nav__search-form').hide();
		$('#top-nav__search-option').click(function() {
			$('#top-nav__search-form').slideToggle("fast", function() {			
		});
  });
  
  $('#main-nav__search-form').hide();
		$('#main-nav__search-option').click(function() {
			$('#main-nav__search-form').slideToggle("fast", function() {			
		});
  });
  
}());