$(document).ready(function(){
    $("button").click(function(){
	var data = {}; 
	data['equation'] = $('#inputField').val();
	var jsonData = [];
	jsonData.push(data);
        $.ajax({
			url: "http://api.calculator.local/result", 
			dataType: 'json', 
			data: JSON.stringify(data), 
			method: "POST",
			success: function(result){
            			$('#inputField').val(result['answer']);
        		}
	});
    });
});
