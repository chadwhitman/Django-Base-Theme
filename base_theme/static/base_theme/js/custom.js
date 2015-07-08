// Place any custom jQuery here //

(function () {
	$('.header__nav__search').hide();
		$('#search__glyph__icon__header').click(function() {
			$('.header__nav__search').slideToggle("fast", function() {			
		});
  });
  
  $('.main-nav .header__nav__search').hide();
		$('.main-nav #search__glyph__icon__main_nav').click(function() {
			$('.main-nav .header__nav__search').slideToggle("fast", function() {			
		});
  });
  
}());