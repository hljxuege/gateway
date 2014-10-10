$(document).ready(function(){
	$('.menu-title').click(function(){
		var title = $(this).html();
		if (title == 'Home'){
			$('#content-center').html($('#content-home').html())
		}
		if (title == 'Contact'){
			$('#content-center').html($('#content-contact').html())
		}
		if (title == 'About'){
			$('#content-center').html($('#content-about').html())
		}

	});
	$('.close-message').click(function(){
		var content = $(this).parent();
		$(content).remove();
	});
});
