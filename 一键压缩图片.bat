@echo off
chcp 65001 > nul

:: ���ñ���
title ͼƬѹ��������

:: ��ȡPython�ű�������·�����������ͱ�bat�ļ���ͬһ��Ŀ¼�£�
set PYTHON_SCRIPT_PATH=%~dp0compress_image.py

:: ����Ƿ����ļ�������
if "%~1"=="" (
    echo.
    echo  û���ļ������룡
    echo.
    echo  �뽫һ������ͼƬ�ļ��϶����˽ű�ͼ���ϡ�
    echo.
    goto end
)

:: ѭ����������������ļ�
:loop
if "%~1"=="" goto done
echo.
echo ----------------------------------------------------
echo ���ڴ����ļ�: %~nx1
echo ----------------------------------------------------
python "%PYTHON_SCRIPT_PATH%" "%~1"
shift
goto loop

:done
echo.
echo ==================== ������������� ====================
echo.

:end
pause