<?php

error_reporting(E_ALL);

$target_dir = "/home/tcolgr01/public_html/";
$target_dir = $target_dir . basename( $_FILES["uploadFile"]["name"]);
$uploadOk=1;

(move_uploaded_file($_FILES["uploadFile"]["tmp_name"], $target_dir));

passthru('/home/tcolgr01/public_html/ocrhandler.py ' . escapeshellarg($_FILES["uploadFile"]["name"]) . " 2>&1" );

?>
