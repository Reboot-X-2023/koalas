<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $inputText = $_POST["input_text"];

    // Call your Python script with the input text
    $outputText = shell_exec('python llm_unit.py "' . $inputText . '"');

    // Display the result
    echo "<h2>Input Text:</h2>";
    echo "<p>{$inputText}</p>";
    echo "<h2>Result:</h2>";
    echo "<p>{$outputText}</p>";
}

?>
