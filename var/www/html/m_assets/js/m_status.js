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

function setVariableValue( variable, value ){
	$(".system-variable-value#"+variable).text( value );
}