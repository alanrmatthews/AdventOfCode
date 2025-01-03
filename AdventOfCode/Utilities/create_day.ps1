param (
    [string]$day
)

$testInputPath = Join-Path -Path $PSScriptRoot -ChildPath "../AoC_2015.Tests/inputs"
$inputFileName = "day" + $day + ".txt"
$sampleFileName = "day" + $day + "_sample.txt"

$inputFile = Join-Path -Path $testInputPath -ChildPath $inputFileName
$sampleFile = Join-Path -Path $testInputPath -ChildPath $sampleFileName

Write-Output "Creating files for day $day"
Write-Output $inputFile
Write-Output $sampleFile

New-Item -ItemType File -Path $inputFile -Force
New-Item -ItemType File -Path $sampleFile -Force

$testDaySrc = Join-Path -Path $PSScriptRoot -ChildPath "TestDayTemplate.txt"
$testDayDst = Join-Path -Path $PSScriptRoot -ChildPath "../AoC_2015.Tests/TestDay$day.cs"
Copy-Item -Path $testDaySrc -Destination $testDayDst -Force
(Get-Content -Path $testDayDst) -creplace 'DayX', "Day$day" | Set-Content -Path $testDayDst
(Get-Content -Path $testDayDst) -creplace 'dayX', "day$day" | Set-Content -Path $testDayDst

$daySrc = Join-Path -Path $PSScriptRoot -ChildPath "DayTemplate.txt"
$dayDst = Join-Path -Path $PSScriptRoot -ChildPath "../AoC_2015/Day$day.cs"
Copy-Item -Path $daySrc -Destination $dayDst -Force
(Get-Content -Path $dayDst) -creplace 'DayX', "Day$day" | Set-Content -Path $dayDst
