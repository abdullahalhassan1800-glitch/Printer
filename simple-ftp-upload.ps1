# Simple FTP Upload Script
$ftp = "ftp://151.106.96.65"
$user = "u817827921.ftp"
$pass = "S3lfm@d3"
$local = "E:\Printer\_site"
$remote = "/"

Write-Host "Starting FTP upload..." -ForegroundColor Green

# Create FTP command file
$ftpCommands = @"
$user
$pass
cd /
lcd $local
mput *
bye
"@

$ftpCommands | Out-File -FilePath "ftp_commands.txt" -Encoding ASCII

# Run FTP
ftp -s:ftp_commands.txt $ftp

# Cleanup
Remove-Item ftp_commands.txt

Write-Host "Upload completed!" -ForegroundColor Green
