echo off
color 
title <nul & title AhmeTLK - %DATE% - %TIME%
cls
%APPDIR%chcp.com 65001 >nul

:a
python price.py
pause
goto a