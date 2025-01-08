param (
    [int]$year
)

$directoryPath = "..\Tests\inputs\$year"
if (-Not (Test-Path -Path $directoryPath)) {
    New-Item -ItemType Directory -Path $directoryPath | Out-Null
}

foreach ($day in 1..25) {
    $filePath = "$directoryPath\day$day.txt"
    if (-Not (Test-Path -Path $filePath)) {
        New-Item -ItemType File -Path $filePath | Out-Null
    }
}

$destinationPath = "..\AoC$year"
if (-Not (Test-Path -Path $destinationPath)) {
    New-Item -ItemType Directory -Path $destinationPath | Out-Null
}

$templateFile = "template_day.py"
foreach ($day in 1..25) {
    $destinationFile = "$destinationPath\day$day.py"
    if (-Not (Test-Path -Path $destinationFile)) {
        Copy-Item -Path $templateFile -Destination $destinationFile
        (Get-Content -Path $destinationFile) -replace 'DayX', "Day$day" | Set-Content -Path $destinationFile
    }
}