<?php

require "db.php";

header("Content-Type: application/json");

$num1 = $_POST["num1"] ?? null;
$operator = $_POST["operator"] ?? null;
$num2 = $_POST["num2"] ?? null;


// Get calculator settings from MySQL

$settingsQuery = $conn->query(
    "SELECT decimal_places, angle_mode, theme
     FROM calculator_settings
     LIMIT 1"
);

$settings = $settingsQuery->fetch_assoc();

$decimalPlaces = $settings["decimal_places"];
$angleMode = $settings["angle_mode"];
$theme = $settings["theme"];


if ($num1 === null || $operator === null) {

    echo json_encode([
        "result" => "Error: Missing input"
    ]);

    exit;
}


// Python executable

$python = getenv("PYTHON_EXECUTABLE") ?: "python";

// Python calculator script

$script = dirname(__DIR__) . DIRECTORY_SEPARATOR . "python" . DIRECTORY_SEPARATOR . "calculator.py";


// Build Python command

$command = escapeshellarg($python) . " "
    . escapeshellarg($script) . " "
    . escapeshellarg($num1) . " "
    . escapeshellarg($operator);


if ($num2 !== null && $num2 !== "") {

    $command .= " " . escapeshellarg($num2);
} else {

    $command .= " " . escapeshellarg("");
}


$command .= " " . escapeshellarg($angleMode);


// Run Python

$output = shell_exec($command);


if ($output === null) {

    echo json_encode([
        "result" => "Error: Could not run Python"
    ]);

    exit;
}


// Decode Python JSON result

$data = json_decode($output, true);


if (isset($data["result"]) && is_numeric($data["result"])) {

    $data["result"] = round(
        (float)$data["result"],
        (int)$decimalPlaces
    );
}


// Send theme to JavaScript

$data["theme"] = $theme;


echo json_encode($data);
