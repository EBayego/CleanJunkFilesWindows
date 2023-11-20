@echo off  
Title Clean Junk Files 
set script_dir=%~dp0
set script_path=%script_dir%clean.py
if not exist "%script_path%" (
    echo Python file not found: "%script_path%"
    pause
    exit /b 1
)
python "%script_path%"
pause