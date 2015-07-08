// Place any custom jQuery here //

(function () {
	$('#top-nav__search__glyph .header__search__input-form').hide();
		$('#top-nav__search__glyph').click(function() {
			$('#top-nav__search__glyph .header__search__input-form').slideToggle("fast", function() {			
		});
  });
  
  $('#main-nav__search__glyph .header__search__input-form').hide();
		$('#main-nav__search__glyph').click(function() {
			$('#main-nav__search__glyph .header__search__input-form').slideToggle("fast", function() {			
		});
  });
  
}());