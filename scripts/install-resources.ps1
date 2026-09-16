<#
.SYNOPSIS
Install selected ai-resources into an existing project without overwriting customizations.
.EXAMPLE
.\scripts\install-resources.ps1 -TargetPath C:\Projects\Example -Workflows plan-feature -WhatIf
#>
[CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'Low')]
param(
    [Parameter(Mandatory = $true)][string]$TargetPath,
    [string[]]$Skills = @(),
    [string[]]$Workflows = @(),
    [switch]$Update,
    [string]$Python = 'python'
)
$ErrorActionPreference = 'Stop'
$arguments = @((Join-Path $PSScriptRoot 'install-resources.py'), '--target', $TargetPath)
foreach ($skillName in $Skills) { $arguments += @('--skill', $skillName) }
foreach ($workflowName in $Workflows) { $arguments += @('--workflow', $workflowName) }
if ($Update) { $arguments += '--update' }
if ($WhatIfPreference) {
    $arguments += '--dry-run'
} elseif (-not $PSCmdlet.ShouldProcess($TargetPath, 'Install selected AI resources')) {
    return
}
& $Python @arguments
if ($LASTEXITCODE -ne 0) { throw "Resource installation failed (exit $LASTEXITCODE)." }
