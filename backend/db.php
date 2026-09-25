<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);

$host = "127.0.0.1";
$username = "root";
$password = getenv("DB_PASSWORD");
$database = "calculator_db";
$port = 3307;

$conn = new mysqli(
    $host,
    $username,
    $password,
    $database,
    $port
);

$conn->set_charset("utf8mb4");
