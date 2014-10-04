$( document ).ready(function() {
  	// initialize charts
  	
  	//velocity
  	var vehicleVelocityChart = new SmoothieChart({maxValue:500,minValue:0});
	vehicleVelocityChart.streamTo(document.getElementById("VehicleVelocity"), 1000 /* delay */);
	
	var vehicleVelocity = new TimeSeries();
	setInterval(function() {
	
		$.getJSON('http://' + serverHost + ':' + serverPort + '/api/message.php?messageName=' + 'BusVoltage', 
			function(data) { 
				vehicleVelocity.append(new Date().getTime(), data.messageValue);
			} );
		
	},500);
	
	vehicleVelocityChart.addTimeSeries( vehicleVelocity );
});

function getMessageVal( messageName ){
	// send GET request to update all status vars
	var rval;
	
	$.getJSON('http://' + serverHost + ':' + serverPort + '/api/message.php?messageName=' + messageName, 
		function(data) { 
			rval = data.messageValue;
		});
		
	return rval;
}