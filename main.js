$(document).ready(function(){
	$('#zipFiles').change(function(){
		$('.theFiles').hide();
		$('#'+$(this).val()).show();
	});
});
