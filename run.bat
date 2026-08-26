@echo off
cd /d "%~dp0"
echo Iniciando servidor Django FEPI...
venv\Scripts\python.exe manage.py runserver
pause
