@echo off
setlocal EnableDelayedExpansion

REM =================================================
REM WORKER MODE
REM =================================================
if /I "%~1"=="RUN" (
    set "RUN_MODE=%~2"
    goto :RUN_FOLDER
)

REM =================================================
REM MANUAL LIST OF RUN MODES
REM =================================================
REM set "FOLDERS=Dtheta30dz1dw0.1dtheta30springAngle80 Dtheta30dz1dw0.1dtheta30springAngle81 Dtheta30dz1dw0.1dtheta30springAngle82 Dtheta30dz1dw0.1dtheta30springAngle83 Dtheta30dz1dw0.1dtheta30springAngle84 Dtheta30dz1dw0.1dtheta30springAngle85 Dtheta30dz1dw0.1dtheta30springAngle86 Dtheta30dz1dw0.1dtheta30springAngle87 Dtheta30dz1dw0.1dtheta30springAngle88 Dtheta30dz1dw0.1dtheta30springAngle89"
set "FOLDERS=Dtheta30dz1dw0.1dtheta30springAngle90"
set "ROOT=%~dp0"

echo.
echo Launching jobs...
echo.

for %%F in (%FOLDERS%) do (

    if exist "%ROOT%%%F\" (

        echo Starting %%F

        start "%%F" cmd /k call "%~f0" RUN "%%F"

    ) else (

        echo WARNING: Folder not found:
        echo %ROOT%%%F\

    )
)

echo.
echo All jobs launched.
goto :EOF


:RUN_FOLDER
setlocal EnableDelayedExpansion

REM =================================================
REM PATHS
REM =================================================
set "ROOT=%~dp0"
set "SCRIPT_DIR=%~dp0"
set "RUN_FOLDER=%ROOT%%RUN_MODE%"

if not exist "%RUN_FOLDER%" (
    echo ERROR: Folder not found:
    echo %RUN_FOLDER%
    pause
    exit /b
)

REM =================================================
REM LOG FILE
REM =================================================
for /f "tokens=1-3 delims=:., " %%a in ("%time%") do (
    set HH=%%a
    set MN=%%b
    set SS=%%c
)

set "HH=!HH: =0!"

set "LOG_FILE=%RUN_FOLDER%\run_!HH!!MN!!SS!.log"
set "RUN_LIST=%RUN_FOLDER%\run_list.txt"

REM =================================================
REM START LOG
REM =================================================
(
echo ===============================================
echo Run started on %DATE% %TIME%
echo MODE: %RUN_MODE%
echo ===============================================
) > "%LOG_FILE%"

echo.
echo =====================================
echo Running %RUN_MODE%
echo =====================================

REM =================================================
REM FIND ALL main.xmf FILES RECURSIVELY
REM =================================================
dir /s /b "%RUN_FOLDER%\main.xmf" > "%RUN_LIST%"

for /f %%A in ('find /c /v "" ^< "%RUN_LIST%"') do set TOTAL=%%A

echo Found %TOTAL% runs
echo Found %TOTAL% runs>>"%LOG_FILE%"

if "%TOTAL%"=="0" (
    echo No main.xmf files found.
    echo No main.xmf files found.>>"%LOG_FILE%"
    exit /b
)

REM =================================================
REM RUN LOOP
REM =================================================
set COUNT=0

for /f "usebackq delims=" %%X in ("%RUN_LIST%") do (

    set /a COUNT+=1

    for %%D in ("%%X") do set "RUNDIR=%%~dpD"

    echo.
    echo [%RUN_MODE%] !COUNT!/%TOTAL%
    echo !RUNDIR!

    echo [%RUN_MODE%] !COUNT!/%TOTAL% !RUNDIR!>>"%LOG_FILE%"

    call "%SCRIPT_DIR%_runXMF.cmd" "!RUNDIR!"

    echo Progress: !COUNT!/%TOTAL%
)

REM =================================================
REM END LOG
REM =================================================
(
echo ===============================================
echo Run finished on %DATE% %TIME%
echo Total completed: %TOTAL%
echo ===============================================
)>>"%LOG_FILE%"

echo.
echo [%RUN_MODE%] FINISHED
echo Log file:
echo %LOG_FILE%

pause
exit /b