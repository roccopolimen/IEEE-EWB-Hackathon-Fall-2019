<?php

    if (isset($_POST['submit'])) {
        $crop = $_POST['crop'];
        $cityState = $_POST['city-state'];
        $yields = $_POST['yields'];
        $profit = $_POST['profit'];
        $temperature = $_POST['temperature'];
        $humidity = $_POST['humidity'];
        $pressure = $_POST['pressure'];
        $waterLevel = $_POST['water-level'];
        echo "yo";
    }

    echo = "hi";
    $keys = array('crop', 'city-state', 'yields', 'profit', 'temperature', 'humidity', 'pressure', 'water-level');
    $csv_line = array();
    foreach($keys as $key){
        array_push($csv_line,'' . $_GET[$key]);
    }
    $fname = 'dataset.csv';
    $csv_line = implode(',',$csv_line);
    if(!file_exists($fname)){$csv_line = "\r\n" . $csv_line;}
    $fcon = fopen($fname,'a');
    $fcontent = $csv_line;
    fwrite($fcon,$csv_line);
    fclose($fcon);
?>