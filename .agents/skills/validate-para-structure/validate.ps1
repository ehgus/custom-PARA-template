$ErrorActionPreference = "Stop"

$workspace_root = "c:\Users\labdo\Desktop\BMOL"

$categories = [ordered]@{
    "1_Projects" = "^0[1-4]-([a-zA-Z0-9_\p{L}]+-)*[a-zA-Z0-9_\p{L}]+$"
    "2_Areas" = "^(?!0[1-4]-)([a-zA-Z0-9_\p{L}]+-)+[a-zA-Z0-9_\p{L}]+$"
    "3_Resources" = "^(?!0[1-4]-)([a-zA-Z0-9_\p{L}]+-)+[a-zA-Z0-9_\p{L}]+$"
}

$validationErrors = @()

foreach ($cat in $categories.Keys) {
    $cat_path = Join-Path $workspace_root $cat
    if (-not (Test-Path $cat_path)) {
        continue
    }
    
    $items = Get-ChildItem -Path $cat_path -Directory
    
    foreach ($item in $items) {
        $name_to_check = $item.Name
        
        if ($name_to_check -match ' ') {
            $validationErrors += "[$cat] '$name_to_check' contains spaces. Spaces are forbidden; use underscores (_)."
            continue
        }
        
        $pattern = $categories[$cat]
        if (-not ($name_to_check -match $pattern)) {
            $validationErrors += "[$cat] '$name_to_check' violates naming structure rules. Check strict delimiter rules (hyphens for tags, underscores for spaces)."
        }
    }
}

if ($validationErrors.Count -gt 0) {
    Write-Host "PARA Structure Validation Failed!" -ForegroundColor Red
    foreach ($err in $validationErrors) {
        Write-Host "  - $err" -ForegroundColor Red
    }
    exit 1
} else {
    Write-Host "PARA Structure Validation Passed." -ForegroundColor Green
    exit 0
}
