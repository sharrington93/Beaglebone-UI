<?php // Establish connection to MySQL database $con = 

$con = mysqli_connect("localhost","root","buckeyes","westest");
// Check the connection - not really necessary, but fuck it why not
if (mysqli_connect_errno()) {
	
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
	
}
// Take in the desired messageName
$requestedMessage = $_GET['messageName'];
//echo $requestedMessage;

// Retrieve the desired attributes from the MySQL database
$sql = "SELECT Value
	FROM Messages
	WHERE MsgName = \"$requestedMessage\"
	ORDER BY time ASC
	LIMIT 1"; 
$result = mysqli_query($con ,$sql);

$val = mysqli_fetch_row( $result )[0];

$reply = array( 'messageName' => $requestedMessage,
				'messageValue' => $val,
				'status' => 'fail',
				'unit' => 'fun' );
				
// Required for security checks when running mobile interface cross-domain
header('Access-Control-Allow-Origin: *');			
	
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
