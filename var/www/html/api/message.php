/*
basic structure:
requestedMessage = $_GET['messageName'];

// open mysql link

// query: SELECT value FROM table WHERE messageName = whatever ORDER BY time ASC LIMIT 5

// format as JSON

return

*/

<?php

// Establish connection to MySQL database
$con = mysqli_connect("localhost","my_user","my_password","my_db");

// Check the connection - not really necessary, but fuck it why not
if (mysqli_connect_errno()) {
	
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
	
}

// Take in the desired messageName
$requestedMessage = $_GET['messageName'];

// Retrieve the desired attributes from the MySQL database 
$result = mysql_query($con, "SELECT Value FROM Messages WHERE messageName = '%s' ORDER BY %f ASC LIMIT 1");
$format = sprintf($requestedMessage);

// Get the number of rows in the database
$rowcount = mysqli_num_rows($result)

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

$row = mysqli_fetch_row($result);
print_r(row);

// Free the result set
mysqli_free_result($result);

// Close the connection
mysqli_close($con);

?>