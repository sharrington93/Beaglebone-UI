<?php // Establish connection to MySQL database $con = 

// Take in the desired messageName
$requestedMessage = $_GET['systemName'];

// Required for security checks when running mobile interface cross-domain
header('Access-Control-Allow-Origin: *');	

$output = array();

if ( $requestedMessage = "batteries" ) {
	$variables = array();
	for ($i = 1; $i < 109; $i++) {
		$signalName = "Cell" . $i . "VoltageAndState";
		$variables[] = $signalName;
	}
}
else if ( $requestedMessage = "powertrain" ) {
	$variables = array("IMPPhaseATemp", "PhaseCurrentA", "BusVoltage", "MotorId", "MotorTemp", "MotorVelocity", "MaxCellTemp");
}

else if ( $requestedMessage = "temppressure") {
	$variables = array("ContactorBoxTemp", "ControllerCoolantTemp", "CoolantFlow", "MotorPlateTemp1",
	"MotorPlateTemp2", "MotorTemp", "RadiatorCoolantTemp", "RadiatorAirPressure");
}

foreach( $variables as $messageName) {
	$filename = "/home/cancorder/data/" . $messageName;
	$fileHandle = fopen($filename, "rb");
	$binaryResult = fread($fileHandle, filesize($filename));
	fclose($fileHandle);
	
	$result = unpack("d*", $binaryResult);
	$output[] = array(  "MessageName" 	=> $messageName,
						"MessageTime"	=> $result[1],
						"MessageValue" 	=> $result[2] );
	
}
echo json_encode($output);

?>
