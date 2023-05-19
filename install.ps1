$install_path = "$Env:USERPROFILE\AppData\Roaming\Rime"
$CurrentLocation = Get-Location
$source_path = "$CurrentLocation\"

# Delete
Write-Host "Remove" $install_path "..."
Remove-Item -Force -Recurse $install_path
# Create
Write-Host "Create SymbolicLink, $install_path to $source_path"
New-Item -ItemType Junction -Path $install_path -Target $source_path 
