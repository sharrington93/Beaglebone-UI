<?php 

// Establish connection to MySQL database
$con = mysqli_connect("localhost","root","buckeyes","westest");

// Check the connection - not really necessary, but fuck it why not
if (mysqli_connect_errno()) {
	
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
	
}

// Retrieve the desired attributes from the MySQL database
$sqlHV = "SELECT Value
	FROM Messages
	WHERE MsgName = 'highVoltage'
	ORDER BY time DESC
	LIMIT 1"; 
	
$sqlES = "SELECT Value
	FROM Messages
	WHERE MsgName = 'EStop'
	ORDER BY time DESC
	LIMIT 1"; 
	
$sqlFF = "SELECT Value
	FROM Messages
	WHERE MsgName = 'FrameFault'
	ORDER BY time DESC
	LIMIT 1"; 

// Form a query on each of the retrieved values
$resultHV = mysqli_query($con ,$sqlHV);
$resultES = mysqli_query($con ,$sqlES);
$resultFF = mysqli_query($con ,$sqlFF);

//Set vals to the respective rows
$valHV = mysqli_fetch_row( $resultHV )[0];
$valES = mysqli_fetch_row( $resultES )[0];
$valFF = mysqli_fetch_row( $resultFF )[0];


// Determine the status of desired variables
if ( $valHV == 1 ) {
	$msgHV = "True";
} else if ( $valHV == 0 ) {
	$msgHV = "False";
}

if ( $valES == 1 ) {
	$msgES = "True";
} else if ( $valES == 0 ) {
	$msgES = "False";
}

if ( $valFF == 1 ) {
	$msgFF = "True";
} else if ( $valFF == 0 ) {
	$msgFF = "False";
}
 
// Create multidimensional array
$reply = array( 
	"highVoltage" 	=> 	$msgHV,
	"EStop"			=>	$msgES,
	"FrameFault"	=>	$msgFF
		);
				
// Required for security checks when running mobile interface cross-domain
header('Access-Control-Allow-Origin: *');			
	
// Format code to be output as a json file	
echo json_encode($reply);

// Free the result set
mysql_free_result($resultHV);
mysql_free_result($resultES);
mysql_free_result($resultFF);
// Close the connection
mysql_close($con);
?>
