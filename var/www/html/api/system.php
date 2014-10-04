<?php // Establish connection to MySQL database $con = 

$con = mysqli_connect("localhost","root","buckeyes","westest");
// Check the connection - not really necessary, but fuck it why not
if (mysqli_connect_errno()) {
	
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
	
}
// Take in the desired messageName
$requestedMessage = $_GET['systemName'];
//echo $requestedMessage;

$output = array();

if ( $requestedMessage = "powertrain" ) {

	$variables = ["PhaseAtemp", "BusVoltage", "Motorld", "MotorTemp", "MotorVelocity", "PackTemp", "PackSOC", "PackBalance", "PrechargeCont", "MainCont", "EStop"];

	foreach( $variables as $messageName ) {

		$query = "SELECT Value  FROM System WHERE messageName = ".$messageName";
		$result =
		$data = mysqli_get_row($result);
	}

}

// Retrieve the desired attributes from the MySQL database
$sql = "SELECT Value
	FROM System
	WHERE SysName = \"$requestedMessage\"
	ORDER BY time ASC
	LIMIT 1"; 
$result = mysqli_query($con ,$sql);
$result = mysqli_query($con ,$sql);
$result = mysqli_query($con ,$sql);
$result = mysqli_query($con ,$sql);
$result = mysqli_query($con ,$sql);
$result = mysqli_query($con ,$sql);
$result = mysqli_query($con ,$sql);
$result = mysqli_query($con ,$sql);
$result = mysqli_query($con ,$sql);
$result = mysqli_query($con ,$sql);
$result = mysqli_query($con ,$sql);

$val = mysqli_fetch_row( $result )[0];
$val1 = mysqli_fetch_row( $result )[1];
$val2 = mysqli_fetch_row( $result )[2];
$val3 = mysqli_fetch_row( $result )[3];
$val4 = mysqli_fetch_row( $result )[4];
$val5 = mysqli_fetch_row( $result )[5];
$val6 = mysqli_fetch_row( $result )[6];
$val7 = mysqli_fetch_row( $result )[7];
$val8 = mysqli_fetch_row( $result )[8];
$val9 = mysqli_fetch_row( $result )[9];
$val10 = mysqli_fetch_row( $result )[10];

$powertrain = array
	(
	array($PhaseAtemp => $val, 'status' => 'fail', 'unit' => 'fun'),
	array($BusVoltage => $val1, 'status' => 'fail', 'unit' => 'fun'),	
	array($Motorld => $val2, 'status' => 'fail', 'unit' => 'fun'),
	array($MotorTemp => $val3, 'status' => 'fail', 'unit' => 'fun'),
	array($MotorVelocity => $val4, 'status' => 'fail', 'unit' => 'fun'),
	array($PackTemp => $val5, 'status' => 'fail', 'unit' => 'fun'),
	array($PackSOC => $val6, 'status' => 'fail', 'unit' => 'fun'),
	array($PackBalance => $val7, 'status' => 'fail', 'unit' => 'fun'),
	array($PrechargeCont => $val8, 'status' => 'fail', 'unit' => 'fun'),
	array($MainCont => $val9, 'status' => 'fail', 'unit' => 'fun'),
	array($EStop => $val10, 'status' => 'fail', 'unit' => 'fun'),
	);
				
echo json_encode($reply);

// Get the number of rows in the database
//$row = mysqli_fetch_array($result);
//echo $row;
//$rowcount = mysqli_num_rows($result);
//echo "\nRow: $rowcount";
/*
// Search through database
while($x <= $rowcount) {
	// Seek to row at position x
	mysqli_data_seek($result,$x);
	// Fetch row
	$row = mysqli_fetch_row($result);
	
	// Put the variables into the json file
	file_put_contents('file.json', json_encode($row));
	
	// Increment to next row in database
	$x++;
}
*/

// Free the result set
mysql_free_result($result);
// Close the connection
mysql_close($con);
?>
