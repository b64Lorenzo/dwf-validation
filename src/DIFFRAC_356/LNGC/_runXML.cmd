@echo off
setlocal
title Diffraction Waves Node XMF Validation (Launcher)

REM ---------------------------------------------------------
REM 0) Get directory argument
REM ---------------------------------------------------------
set "DIR=%~1"

if not exist "%DIR%" (
    echo ERROR: Directory not found: %DIR%
    exit /b 1
)

REM ---------------------------------------------------------
REM CLEAN DIRECTORY (remove ALL files and folders except main.input.xml)
REM ---------------------------------------------------------
REM echo Cleaning directory:
REM echo   %DIR%

REM 1) Delete ALL subdirectories
REM for /D %%D in ("%DIR%\*") do (
REM     rmdir /S /Q "%%D"
REM )

REM 2) Delete ALL files except main.input.xml
REM for %%F in ("%DIR%\*") do (
REM     if /I not "%%~nxF"=="main.input.xml" (
REM         del /Q "%%F"
 REM    )
REM )


REM ---------------------------------------------------------
REM 2) Configuration
REM ---------------------------------------------------------
REM set "XMLROOT=C:\Users\LZambelli\Desktop\Marin Programs\diffrac\v3.5.7b"
set "XMLROOT=C:\Users\zambe\OneDrive\Desktop\Marin\v3.5.7b"
set "RUN=DIFFRACSUITE"

REM ---------------------------------------------------------
REM 3) Build command that runs INSIDE the new terminal
REM ---------------------------------------------------------
set "CMDLINE=call "%XMLROOT%\setpath.cmd" ^&^& echo Working directory: %%CD%% ^&^& "%RUN%" main ^>^> terminal_output.log 2^>^&1 ^&^& exit /b %%ERRORLEVEL%%"

REM ---------------------------------------------------------
REM 4) Open new terminal IN THE DIRECTORY and run command
REM ---------------------------------------------------------
start /WAIT "DIFFRAC Simulation" /D "%DIR%" cmd /C %CMDLINE%

REM ---------------------------------------------------------
REM 5) Close launcher
REM ---------------------------------------------------------

exit /b 0



