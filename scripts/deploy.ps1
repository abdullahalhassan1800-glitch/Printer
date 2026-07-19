param(
    [Parameter(Mandatory=$true)]
    [string]$FtpHost,

    [Parameter(Mandatory=$true)]
    [string]$FtpUser,

    [Parameter(Mandatory=$true)]
    [string]$FtpPass,

    [string]$SiteDir = "_site",

    [switch]$SkipBuild
)

$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $PSScriptRoot
$SitePath = Join-Path $ProjectRoot $SiteDir

if (-not (Test-Path $SitePath)) {
    Write-Host "[ERROR] Site directory not found: $SitePath" -ForegroundColor Red
    Write-Host "Run 'bundle exec jekyll build' first, or specify -SiteDir" -ForegroundColor Yellow
    exit 1
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " FTP Deploy - Printer Services Pro" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Host:   $FtpHost"
Write-Host "User:   $FtpUser"
Write-Host "Source: $SitePath"
Write-Host ""

if ($SkipBuild) {
    Write-Host "[1/3] Skipping build (using existing _site)" -ForegroundColor Yellow
} else {
    Write-Host "[1/3] Building Jekyll site..." -ForegroundColor Yellow
    Push-Location $ProjectRoot
    try {
        bundle exec jekyll build 2>&1 | Out-Null
        if ($LASTEXITCODE -ne 0) {
            Write-Host "[ERROR] Jekyll build failed" -ForegroundColor Red
            exit 1
        }
        Write-Host "  Build complete." -ForegroundColor Green
    } finally {
        Pop-Location
    }
}

function New-FtpClient {
    param([string]$FtpHost, [int]$Port = 21)
    $client = New-Object System.Net.Sockets.TcpClient($FtpHost, $Port)
    $stream = $client.GetStream()
    $reader = New-Object System.IO.StreamReader($stream)
    $writer = New-Object System.IO.StreamWriter($stream)
    $writer.AutoFlush = $true
    $banner = $reader.ReadLine()
    return @{
        Client = $client
        Stream = $stream
        Reader = $reader
        Writer = $writer
        Banner = $banner
    }
}

function Send-FtpCmd {
    param($Conn, [string]$Cmd)
    $Conn.Writer.WriteLine($Cmd)
}

function Read-FtpResp {
    param($Conn)
    $lines = @()
    $line = $Conn.Reader.ReadLine()
    $lines += $line
    if ($line -match '^\d{3}-') {
        while ($true) {
            $line = $Conn.Reader.ReadLine()
            $lines += $line
            if ($line -match '^\d{3} ') { break }
        }
    }
    return ($lines -join "`n")
}

function Parse-Pasv($Response) {
    if ($Response -match "\((\d+),(\d+),(\d+),(\d+),(\d+),(\d+)\)") {
        $ip = "$($Matches[1]).$($Matches[2]).$($Matches[3]).$($Matches[4])"
        $port = [int]$Matches[5] * 256 + [int]$Matches[6]
        return @{ IP = $ip; Port = $port }
    }
    return $null
}

Write-Host "[2/3] Uploading to FTP..." -ForegroundColor Yellow

$Conn = New-FtpClient -FtpHost $FtpHost
Write-Host "  Connected: $($Conn.Banner)" -ForegroundColor Gray

Send-FtpCmd $Conn "USER $FtpUser"
$userResp = Read-FtpResp $Conn
Send-FtpCmd $Conn "PASS $FtpPass"
$passResp = Read-FtpResp $Conn

if ($passResp -notmatch "^230") {
    Write-Host "[ERROR] Login failed: $passResp" -ForegroundColor Red
    $Conn.Client.Close()
    exit 1
}
Write-Host "  Logged in." -ForegroundColor Green

Send-FtpCmd $Conn "TYPE I"
$typeResp = Read-FtpResp $Conn

$AllFiles = Get-ChildItem -Path $SitePath -Recurse -File
$TotalFiles = $AllFiles.Count
$Uploaded = 0
$Failed = 0
$Index = 0
$StartTime = Get-Date

function Ensure-FtpDir {
    param($ConnObj, [string]$RemotePath)
    Send-FtpCmd $ConnObj "CWD /$RemotePath"
    $cwdResp = Read-FtpResp $ConnObj
    if ($cwdResp -notmatch "^250") {
        Send-FtpCmd $ConnObj "MKD /$RemotePath"
        $mkdResp = Read-FtpResp $ConnObj
    }
    Send-FtpCmd $ConnObj "CWD /"
    Read-FtpResp $ConnObj
}

foreach ($File in $AllFiles) {
    $Index++
    $RelativePath = $File.FullName.Substring($SitePath.Length + 1).Replace('\', '/')
    $Progress = [math]::Round(($Index / $TotalFiles) * 100)

    Write-Host -NoNewline "`r  [$Index/$TotalFiles] ($Progress%) Uploading: $RelativePath                                   "

    try {
        $parts = $RelativePath -split '/'
        if ($parts.Length -gt 1) {
            $dirPath = $parts[0..($parts.Length - 2)] -join '/'
            $dirs = $dirPath -split '/'
            $currentDir = ""
            foreach ($d in $dirs) {
                if ($currentDir) { $currentDir = "$currentDir/$d" } else { $currentDir = $d }
                Ensure-FtpDir -ConnObj $Conn -RemotePath $currentDir
            }
        }

        Send-FtpCmd $Conn "PASV"
        $pasvResp = Read-FtpResp $Conn
        $pasvInfo = Parse-Pasv $pasvResp
        if (-not $pasvInfo) { throw "Could not parse PASV response: $pasvResp" }

        $dataClient = New-Object System.Net.Sockets.TcpClient($pasvInfo.IP, $pasvInfo.Port)
        $dataStream = $dataClient.GetStream()

        Send-FtpCmd $Conn "STOR /$RelativePath"
        $storResp = Read-FtpResp $Conn

        $fileStream = [System.IO.File]::OpenRead($File.FullName)
        try {
            $fileStream.CopyTo($dataStream)
        } finally {
            $fileStream.Close()
            $dataStream.Close()
            $dataClient.Close()
        }

        $endResp = Read-FtpResp $Conn
        $Uploaded++
    } catch {
        $Failed++
        Write-Host ""
        Write-Host "  [FAIL] $RelativePath - $($_.Exception.Message)" -ForegroundColor Red
    }
}

Send-FtpCmd $Conn "QUIT"
Read-FtpResp $Conn
$Conn.Client.Close()

$Elapsed = (Get-Date) - $StartTime

Write-Host ""
Write-Host "[3/3] Deploy complete!" -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Results" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Uploaded: $Uploaded files" -ForegroundColor Green
if ($Failed -gt 0) {
    Write-Host "  Failed:   $Failed files" -ForegroundColor Red
}
Write-Host "  Time:     $([math]::Round($Elapsed.TotalSeconds, 1))s" -ForegroundColor Cyan
Write-Host "  URL:      https://printerandservices.pro" -ForegroundColor Cyan
Write-Host ""
