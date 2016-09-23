/*
	@ Harris Christiansen (Harris@HarrisChristiansen.com)
	2016-09-18
	Project: HTML5 Boilerplate
*/


$(document).ready(function() { 
	$(".sortable").tablesorter(); 
});

$('.validate').bValidator();

$(".datepicker").datepicker({
	dateFormat: 'yy-mm-dd',
});