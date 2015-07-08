// Place any custom jQuery here //

(function () {
	$('#header__nav__search').hide();
		$('.search__glyph__icon.header').click(function() {
			$('.search__glyph__icon.header').slideToggle("fast", function() {			
		});
  });
  
  $('#main_nav__search').hide();
		$('.search__glyph__icon.main_nav').click(function() {
			$('.search__glyph__icon.main_nav').slideToggle("fast", function() {			
		});
  });
  
}());