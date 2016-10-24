/*
	@ Harris Christiansen (Harris@HarrisChristiansen.com)
	2016-09-18
	Project: CSCapstone Marketplace
*/


$(document).ready(function() { 
	$(".sortable").tablesorter();
	$('.validate').bValidator();

	$(".datepicker").datepicker({
		dateFormat: 'yy-mm-dd',
	});
});