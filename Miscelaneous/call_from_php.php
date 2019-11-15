<?php
	$latitude = 38.0;
	$longitude=-122.0;
    $command = escapeshellcmd('python find_location.py'.$latitude.' '.$longitude. .'> temp.txt');
    $output = shell_exec($command);
    echo $output;
?>