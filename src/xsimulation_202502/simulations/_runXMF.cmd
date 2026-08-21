@echo off
setlocal EnableDelayedExpansion
title Diffraction Waves Node XMF Validation

REM ---------------------------------------------------------
REM 0) DIRECTORY INPUT FROM OUTSIDE
REM ---------------------------------------------------------
set "DIR=%~1"

echo Initializing XSimulation environment...
echo Working directory: %DIR%

REM ---------------------------------------------------------
REM 1) Environment setup
REM ---------------------------------------------------------
REM set "XMFROOT=C:\Users\LZambelli\Desktop\Marin Programs\xsimulation_2502"
set "XMFROOT=C:\Users\zambe\OneDrive\Desktop\Marin\xsimulation\2026.02\eoe"

REM ft or xsfviewer
set "RUN=ft"

REM ---------------------------------------------------------
REM 2) Load XMF environment from setpath.cmd
REM ---------------------------------------------------------
call "%XMFROOT%\setpath.cmd"
set "MSTNFYLEVEL=debug"
set "MSTNFYFLUSH=1"
REM ---------------------------------------------------------
REM 3) Run simulation in the given folder
REM ---------------------------------------------------------
echo Starting simulation...

echo Running:
echo %RUN% -c %DIR%\main.xmf -R %DIR% -E progress -o graph.txt
echo.

%RUN% -c %DIR%\main.xmf -R %DIR% -E progress -o graph.txt ^
    >> "%DIR%\terminal_output.log" 2>&1


REM ---------------------------------------------------------
REM 4) Check for errors
REM ---------------------------------------------------------
if %ERRORLEVEL% NEQ 0 (
    echo ERROR occurred in %DIR%
) else (
    echo Simulation completed successfully in %DIR%
)

REM ---------------------------------------------------------
REM 5) Keep window open so you can read the error
REM ---------------------------------------------------------
echo.
timeout /t 3 >nul
exit /b %ERRORLEVEL%



