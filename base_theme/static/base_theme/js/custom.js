// Place any custom jQuery here //

(function () {
	$('.header__nav__search.header').hide();
		$('#search__glyph__icon__header').click(function() {
			$('.header__nav__search.header').slideToggle("fast", function() {			
		});
  });
  
  $('.main-nav .header__nav__search.main-nav').hide();
		$('.main-nav #search__glyph__icon__main_nav').click(function() {
			$('.main-nav .header__nav__search.main-nav').slideToggle("fast", function() {			
		});
  });
  
}());