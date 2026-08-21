@echo off
setlocal EnableDelayedExpansion

set "SCRIPT_DIR=%~dp0"

for /f "delims=" %%i in ('dir /b /a-d /s main.input.xml') do (
    set "DIFFRAC_DIR=%%~dpi"

    echo ---------------------------------------------------------
    echo Running simulation in:
    echo   !DIFFRAC_DIR!
    echo ---------------------------------------------------------

    call "%SCRIPT_DIR%_runXML.cmd" "!DIFFRAC_DIR!"

    echo Finished simulation for:
    echo   !DIFFRAC_DIR!
    echo.
)

endlocal