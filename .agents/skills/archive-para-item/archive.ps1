param (
    [Parameter(Mandatory=$true)]
    [string]$TargetPath
)

$WorkspaceRoot = (Get-Item "$PSScriptRoot\..\..\..").FullName

$AbsTarget = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($TargetPath)

if ($AbsTarget.EndsWith('.lnk', [System.StringComparison]::OrdinalIgnoreCase)) {
    try {
        $WshShell = New-Object -ComObject WScript.Shell
        $Shortcut = $WshShell.CreateShortcut($AbsTarget)
        if ($Shortcut.TargetPath) {
            $AbsTarget = $Shortcut.TargetPath
        }
    } catch {}
}

if (-not (Test-Path -LiteralPath $AbsTarget)) {
    Write-Host "Error: Target path does not exist: $AbsTarget"
    exit 1
}

if (-not $AbsTarget.StartsWith($WorkspaceRoot, [System.StringComparison]::InvariantCultureIgnoreCase)) {
    Write-Host "Error: Target must be inside the workspace root: $WorkspaceRoot"
    exit 1
}

$RelPath = $AbsTarget.Substring($WorkspaceRoot.Length).TrimStart('\')
$Parts = $RelPath.Split('\')

if ($Parts.Length -lt 2 -or ($Parts[0] -notin @('1_Projects', '2_Areas', '3_Resources'))) {
    Write-Host "Error: Target must be a direct child of 1_Projects, 2_Areas, or 3_Resources. Got: $RelPath"
    exit 1
}

$Category = $Parts[0]
$ItemName = $Parts[-1]

$Now = Get-Date
$Quarter = [math]::Truncate(($Now.Month - 1) / 3) + 1
$Prefix = "$($Now.Year)-Q$Quarter-"

$NewItemName = $Prefix + $ItemName

$ArchiveDir = Join-Path $WorkspaceRoot "4_Archives\$Category"
if (-not (Test-Path -LiteralPath $ArchiveDir)) {
    New-Item -ItemType Directory -Path $ArchiveDir -Force | Out-Null
}

$NewAbsPath = Join-Path $ArchiveDir $NewItemName

if (Test-Path -LiteralPath $NewAbsPath) {
    Write-Host "Error: Destination already exists: $NewAbsPath"
    exit 1
}

try {
    Move-Item -LiteralPath $AbsTarget -Destination $NewAbsPath -ErrorAction Stop
    Write-Host "Successfully archived '$ItemName' to '$NewAbsPath'"
} catch {
    Write-Host "Failed to move: $_"
    exit 1
}
