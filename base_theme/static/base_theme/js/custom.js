// Place any custom jQuery here //

(function () {
	$('.header__search__input-form').hide();
		$('#top-nav__search__glyph').click(function() {
			$('.header__search__input-form').slideToggle("fast", function() {			
		});
  });
  
  $('.main-nav .header__search__input-form').hide();
		$('.main-nav #main-nav__search__glyph').click(function() {
			$('.main-nav .header__search__input-form').slideToggle("fast", function() {			
		});
  });
  
}());