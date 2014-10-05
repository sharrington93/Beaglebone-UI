$( document ).ready(function() {
	serverHost = '192.168.7.35';
	serverPort = '80';
  	// automatically update system status
  	updateAll();
  	
  	setInterval(function() {
  		updateAll();
  		updateVehicleStatus();
  	}, 1000);
} );

function updateMessage( messageName ){
	// send GET request to update all status vars
	$.getJSON('http://' + serverHost + ':' + serverPort + '/api/message.php?messageName=' + messageName, 
		function(data) { 
		
			varName = data.messageName;
			value = data.messageValue;
			status = data.status;
			
			$(".system-variable-value#"+varName).text( value );
			
			switch( status ){
				case "Warn":
					$(".system-variable-name#"+varName).css( 'color', 'yellow' );
					break;
					
				case "Fail":
					$(".system-variable-name#"+varName).css( 'color', 'red' );
					break;
					
				default:
					$(".system-variable-name#"+varName).css( 'color', '' );
					break;
			}
		
		} );
}

function updateVehicleStatus( ){
	// Update the vehicle status variables that trigger popovers (frame fault, HV state, E-stop)
	$.getJSON('http://' + serverHost + ':' + serverPort + '/api/vehicleStatus.php', 
		function(data) { 
			if( data.highVoltage == "True" ){
				$(".alert-hv").removeClass("hidden");
			} else {
				$(".alert-hv").addClass("hidden");
			}
			
			if( data.FrameFault == "True"){
				$(".alert-framefault").removeClass("hidden");
			} else {
				$(".alert-framefault").addClass("hidden");
			}
			
			if( data.EStop == "True"){
				$(".alert-estop").removeClass("hidden");
			} else {
				$(".alert-estop").addClass("hidden");
			}
	} );
}

function updateAll( ){
	// send GET request to update all status vars
	$.getJSON('http://' + serverHost + ':' + serverPort + '/api/system.php?systemName=powertrain', 
		function(data) { 
			for(var i = 0; i < data.length; i++){
				varName = data[i].messageName;
				value 	= data[i].messageValue;
				status 	= data[i].messageStatus;
	
				$(".system-variable-value#"+varName).text( value );
			
				switch( status ){
					case "Warn":
						$(".system-variable-name#"+varName).css( 'color', 'yellow' );
						break;
					
					case "Fail":
						$(".system-variable-name#"+varName).css( 'color', 'red' );
						break;
					
					default:
						$(".system-variable-name#"+varName).css( 'color', '' );
						break;
				}
			}
		
		} );
}

function setSystemStatus( system, status ){
	system = system.toLowerCase();
	switch( status ){
		case "OK":
			$(".system-status-indicator#" + system).css("background-color", "green");
			break;
		case "Warn":
			$(".system-status-indicator#" + system).css("background-color", "yellow");
			break;
		case "Fail":
			$(".system-status-indicator#" + system).css("background-color", "red");
			break;
		case "NoData":
			$(".system-status-indicator#" + system).css("background-color", "gray");
			// hmm what else should we do here
		default:
			console.log("updateSystemStatus() called without a valid status");
	}
}