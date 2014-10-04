<?php

echo '<pre>';
print_r( $_GET );
echo '</pre>';

/*
basic structure:
requestedMessage = $_GET['messageName'];

// open mysql link

// query: SELECT value FROM table WHERE messageName = whatever ORDER BY time ASC LIMIT 5

// format as JSON

return

*/

?>