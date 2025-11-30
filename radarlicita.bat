@echo off
title Radar Licita - Modo Apresentacao
color 0A

echo.
echo ========================================
echo   RADAR LICITA - MODO APRESENTACAO
echo ========================================
echo.

REM Ativa o ambiente virtual
if exist venv\Scripts\activate.bat (
    echo [1/3] Ativando ambiente virtual...
    call venv\Scripts\activate.bat
) else (
    echo ERRO: Ambiente virtual nao encontrado!
    echo Execute: python -m venv venv
    pause
    exit /b 1
)

echo [2/3] Instalando dependencias da interface...
pip install -q flask flask-socketio python-socketio

echo [3/3] Iniciando servidor web...
echo.
python app.py

pause
