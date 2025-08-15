
$ErrorActionPreference = "Stop"
$epheDir = "sweph\ephe"
New-Item -ItemType Directory -Force -Path $epheDir | Out-Null
Set-Location $epheDir

$baseUrl = "https://www.astro.com/ftp/swisseph/ephe"
$files = @("sepl_19.se1","semo_19.se1","sepl_20.se1","semo_20.se1")

foreach ($f in $files) {
    $url = "$baseUrl/$f"
    Write-Host "Downloading $url"
    Invoke-WebRequest -Uri $url -OutFile $f
}

Write-Host "Done. Files in $(Get-Location)"
Get-ChildItem sepl_19.se1, semo_19.se1, sepl_20.se1, semo_20.se1 | Format-Table Name, Length
