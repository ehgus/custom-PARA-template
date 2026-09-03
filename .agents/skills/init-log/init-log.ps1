param (
    [Parameter(Mandatory=$true)]
    [string]$TargetPath
)

$ErrorActionPreference = "Stop"

$WorkspaceRoot = (Get-Item "$PSScriptRoot\..\..\..").FullName

$AbsTarget = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($TargetPath)

if ($AbsTarget.EndsWith('.lnk', [System.StringComparison]::OrdinalIgnoreCase)) {
    try {
        $WshShell = New-Object -ComObject WScript.Shell
        $Shortcut = $WshShell.CreateShortcut($AbsTarget)
        if ($Shortcut.TargetPath) {
            $AbsTarget = $Shortcut.TargetPath
        }
    } catch {
        Write-Error "Failed to resolve shortcut: $_"
        exit 1
    }
}

if (-not (Test-Path -LiteralPath $AbsTarget)) {
    Write-Error "Target path does not exist: $AbsTarget"
    exit 1
}

if (-not $AbsTarget.StartsWith($WorkspaceRoot, [System.StringComparison]::InvariantCultureIgnoreCase)) {
    Write-Error "Target must be inside the workspace root: $WorkspaceRoot"
    exit 1
}

$RelPath = $AbsTarget.Substring($WorkspaceRoot.Length).TrimStart('\')
$Parts = $RelPath.Split('\')

if ($Parts.Length -lt 2 -or ($Parts[0] -notin @('1_Projects', '2_Areas', '3_Resources'))) {
    Write-Error "Target must be located inside 1_Projects, 2_Areas, or 3_Resources. Got: $RelPath"
    exit 1
}

$LogDir = Join-Path $AbsTarget "00-log"
$IssuesDir = Join-Path $LogDir "issues"
$DecisionsDir = Join-Path $LogDir "decisions"

try {
    if (-not (Test-Path -LiteralPath $IssuesDir)) {
        New-Item -ItemType Directory -Path $IssuesDir -Force | Out-Null
    }
    if (-not (Test-Path -LiteralPath $DecisionsDir)) {
        New-Item -ItemType Directory -Path $DecisionsDir -Force | Out-Null
    }

    $IssuesGitKeep = Join-Path $IssuesDir ".gitkeep"
    if (-not (Test-Path -LiteralPath $IssuesGitKeep) -and (Get-ChildItem -LiteralPath $IssuesDir).Count -eq 0) {
        New-Item -ItemType File -Path $IssuesGitKeep -Force | Out-Null
    }

    $DecisionsGitKeep = Join-Path $DecisionsDir ".gitkeep"
    if (-not (Test-Path -LiteralPath $DecisionsGitKeep) -and (Get-ChildItem -LiteralPath $DecisionsDir).Count -eq 0) {
        New-Item -ItemType File -Path $DecisionsGitKeep -Force | Out-Null
    }

    Write-Host "Successfully initialized 00-log directory at: $LogDir" -ForegroundColor Green
    exit 0
} catch {
    Write-Error "Failed to initialize 00-log directory: $_"
    exit 1
}
