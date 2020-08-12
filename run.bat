@echo off
SET PYTHON_PATH=C:\Python27.16
PATH %PYTHON_PATH%;%PYTHON_PATH%\Scripts;%PYTHON_PATH%\Lib\site-packages;%PYTHON_PATH%\Lib\site-packages\PyQt4;%PATH%;

python %~dp0\run.py
