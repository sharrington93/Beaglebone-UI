$( document ).ready(function() {
	serverHost = '192.168.7.35';
	serverPort = '80';
  	// automatically update system status
  	
});

function updateMessage( var ){
	// send GET request to update all status vars
	$.get('http://' + serverHost + ':' + serverPort + '/api/message.php?messageName=' + var, 
		function(data) { 
		
			varName = data.messageName;
			value = data.messageValue;
			status = data.status;
			
			$("system-variable-value#"+varName).text( value );
		
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