/*
	@ Harris Christiansen (Harris@HarrisChristiansen.com)
	File Created: September 18, 2016
	Project: CSCapstone Marketplace
*/


$(document).ready(function() { 
	$(".sortable").tablesorter();
	$('.validate').bValidator();

	$(".datepicker").datepicker({
		dateFormat: 'yy-mm-dd',
	});

	$(".tagSelect").select2({
		tags: true,
		tokenSeparators: [',', ' ']
	});
});